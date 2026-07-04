import argparse
import psutil
import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("System Resource Monitor")  # MCP sunucusunu başlat

@mcp.tool() # Yapay zekanın kullanacağı aracı (tool) tanımla
def mcp_tespit() -> str:
    """Sistemin anlık CPU, RAM ve Disk istatistiklerini getirir."""
    cpu_percent = psutil.cpu_percent(interval=1) # CPU 
    
    memory = psutil.virtual_memory()   # RAM 
    mem_total_gb = memory.total / (1024 ** 3)
    mem_used_gb = memory.used / (1024 ** 3)

    disk = psutil.disk_usage('/')      # Disk 
    disk_total_gb = disk.total / (1024 ** 3)
    disk_used_gb = disk.used / (1024 ** 3)

    stats = {     # Sonuçlar
        "cpu": {"usage_percent": cpu_percent},
        "memory": {
            "total_gb": round(mem_total_gb, 2),
            "used_gb": round(mem_used_gb, 2),
            "usage_percent": memory.percent
        },
        "disk": {
            "total_gb": round(disk_total_gb, 2),
            "used_gb": round(disk_used_gb, 2),
            "usage_percent": disk.percent
        }
    }
    return json.dumps(stats, indent=2)  # JSON formatına çeviriyoruz

if __name__ == "__main__":
    # Komut satırı ayarları (stdio vs sse)
    parser = argparse.ArgumentParser()
    parser.add_argument("--transport", choices=["stdio", "sse"], default="stdio")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    
    # Seçilen moda göre sunucuyu çalıştır
    if args.transport == "sse":
        print(f"SSE modu aktif. Port: {args.port}")
        mcp.run(transport="sse", port=args.port)
    else:
        mcp.run(transport="stdio")
