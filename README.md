# Stomatologiya Klinikasi - Deploy qo'llanmasi

## Local serverda ishga tushirish

1. **Virtual environment yaratish:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

2. **Paketlarni o'rnatish:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ma'lumotlar bazasini yaratish:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Serverni ishga tushirish:**
   ```bash
   python manage.py runserver
   ```

## Production deploy (Heroku)

1. **Heroku CLI o'rnatish**

2. **Git repository yaratish:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

3. **Heroku app yaratish:**
   ```bash
   heroku create your-app-name
   ```

4. **Environment variables sozlash:**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   ```

5. **Deploy qilish:**
   ```bash
   git push heroku main
   ```

## Boshqa hosting variantlari

### DigitalOcean App Platform
- Repository ni ulang
- Environment variables qo'shing
- Deploy tugmasini bosing

### Railway
- GitHub repository ni ulang
- Avtomatik deploy

### Vercel (statik fayllar uchun)
- Next.js ga o'tkazish kerak

## Muhim eslatmalar

- `DEBUG = False` production da
- `SECRET_KEY` ni himoya qiling
- Database URL environment variable orqali bering
- SSL sertifikat o'rnating
- Regular backup qiling

## Domain ulash

1. Domain provider da DNS sozlang
2. Heroku da custom domain qo'shing
3. SSL sertifikat avtomatik yaratiladi