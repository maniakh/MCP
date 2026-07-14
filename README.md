<img width="1424" height="752" alt="Image" src="https://github.com/user-attachments/assets/73a8abc0-e119-45ff-b36d-6f18548ded09" />

# mcp-tespit

Bu, yapay zeka asistanlarinin (ornegin Claude) bilgisayarinizin anlik CPU, RAM ve Disk kullanimini gorebilmesini saglayan Model Context Protocol (MCP) aracidir.

## Kurulum

Gerekli kutuphaneleri kurun:
   ```bash
   pip install -r requirements.txt
   ```

## Server'ı Ayağa Kaldırma

Sunucuyu iki farklı modda çalıştırabilirsiniz:

**1. Claude Desktop ve MCP İstemcileri İçin (STDIO - Varsayılan)**
Bu modda sunucu arkaplanda doğrudan standart I/O üzerinden iletişim kurar.
```bash
python server.py --transport stdio
```

**2. Web/Ağ Üzerinden Erişmek İçin (SSE)**
Eğer MCP sunucunuza normal bir sunucu gibi ayağa kalkıp bir port (örn: 8000) üzerinden çalışmasını isterseniz:
```bash
python server.py --transport sse --port 8000
```
*(Bu komutu girdiğinizde sunucu 8000 portunda dinlemeye başlar ve log verir.)*

## Claude Desktop'a Ekleme

Claude uygulamasinin ayarlarindaki konfigürasyon dosyasina sunu ekleyin (yolu kendi bilgisayariniza gore duzeltin):

```json
{
  "mcpServers": {
    "sysinfo": {
      "command": "python",
      "args": ["C:/tam/yol/server.py", "--transport", "stdio"]
    }
  }
}
```
<img width="809" height="268" alt="Image" src="https://github.com/user-attachments/assets/ab76f25a-198f-4d85-a6f3-f4cbe3137d62" />
<img width="264" height="428" alt="Image" src="https://github.com/user-attachments/assets/59687070-d5a3-42ed-ac53-9246b067e081" />

**[MCP Blog Yazısını Oku](https://enableroot.com/blog/mcp)**
