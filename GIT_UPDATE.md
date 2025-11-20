# دليل رفع التحديثات إلى GitHub

## 📋 خطوات رفع التحديثات

### الطريقة 1: استخدام Git Command Line

#### 1. التحقق من حالة الملفات:
```bash
git status
```

#### 2. إضافة جميع الملفات الجديدة والمحدثة:
```bash
git add .
```

أو إضافة ملفات محددة:
```bash
git add app.py requirements.txt render.yaml .gitignore runtime.txt DEPLOY.md
```

#### 3. عمل commit للتحديثات:
```bash
git commit -m "Add OFB and CTR encryption, prepare for Render deployment"
```

أو رسالة أكثر تفصيلاً:
```bash
git commit -m "Update: Add OFB and CTR encryption modes, Render deployment config, and documentation"
```

#### 4. رفع التحديثات إلى GitHub:
```bash
git push origin main
```

أو إذا كان الفرع اسمه `master`:
```bash
git push origin master
```

---

### الطريقة 2: استخدام GitHub Desktop

1. **افتح GitHub Desktop**
2. **ستظهر التغييرات تلقائياً** في الشاشة الرئيسية
3. **اكتب رسالة commit** في المربع السفلي:
   ```
   Add OFB and CTR encryption, prepare for Render deployment
   ```
4. **اضغط على "Commit to main"** (أو master)
5. **اضغط على "Push origin"** لرفع التحديثات

---

### الطريقة 3: استخدام VS Code

1. **افتح VS Code** في مجلد المشروع
2. **اذهب إلى Source Control** (أيقونة Git في الشريط الجانبي)
3. **ستظهر جميع الملفات المحدثة**
4. **اضغط على "+" بجانب "Changes"** لإضافة جميع الملفات
5. **اكتب رسالة commit** في المربع العلوي
6. **اضغط على ✓ (Commit)**
7. **اضغط على "..." → "Push"** لرفع التحديثات

---

## 📝 الملفات الجديدة التي سيتم رفعها:

### ملفات جديدة:
- ✅ `crypto_modules/ofb_encryption.py`
- ✅ `crypto_modules/ofb_decryption.py`
- ✅ `crypto_modules/ctr_encryption.py`
- ✅ `crypto_modules/ctr_decryption.py`
- ✅ `render.yaml`
- ✅ `.gitignore`
- ✅ `runtime.txt`
- ✅ `MANUAL.md`
- ✅ `DEPLOY.md`
- ✅ `GIT_UPDATE.md` (هذا الملف)

### ملفات محدثة:
- ✅ `app.py` (إضافة OFB وCTR + إعدادات Render)
- ✅ `requirements.txt` (إضافة gunicorn)
- ✅ `README.md` (إضافة OFB وCTR)
- ✅ `FLOWCHART.md` (إضافة OFB وCTR)

---

## 🔍 التحقق من التحديثات

بعد الرفع، يمكنك التحقق من:

1. **افتح repository على GitHub**
2. **تحقق من أن جميع الملفات موجودة**
3. **تحقق من آخر commit** - يجب أن يحتوي على رسالتك

---

## ⚠️ ملاحظات مهمة

### إذا ظهرت رسالة خطأ:

#### خطأ: "fatal: not a git repository"
**الحل:** يجب تهيئة Git أولاً:
```bash
git init
git remote add origin https://github.com/username/repo-name.git
```

#### خطأ: "Permission denied"
**الحل:** 
- تأكد من تسجيل الدخول إلى GitHub
- تحقق من صلاحيات الوصول للـ repository

#### خطأ: "Updates were rejected"
**الحل:** 
- قد يكون هناك تحديثات على GitHub لم تسحبها
- اسحب التحديثات أولاً:
```bash
git pull origin main
```
- ثم ارفع التحديثات مرة أخرى:
```bash
git push origin main
```

---

## 📋 سلسلة الأوامر الكاملة (Copy & Paste)

إذا كان repository موجود بالفعل:

```bash
# التحقق من الحالة
git status

# إضافة جميع الملفات
git add .

# عمل commit
git commit -m "Add OFB and CTR encryption modes, Render deployment config, and documentation"

# رفع التحديثات
git push origin main
```

---

## 🎯 رسائل Commit مقترحة:

### رسالة قصيرة:
```
Add OFB and CTR encryption, prepare for Render deployment
```

### رسالة متوسطة:
```
Update: Add OFB and CTR encryption modes, Render deployment configuration, and comprehensive documentation
```

### رسالة مفصلة:
```
feat: Add OFB and CTR encryption modes

- Add OFB (Output Feedback) encryption and decryption
- Add CTR (Counter) encryption and decryption
- Update app.py to include new encryption methods
- Add Render deployment configuration (render.yaml, runtime.txt)
- Add gunicorn for production server
- Update documentation (README, FLOWCHART, MANUAL)
- Add deployment guide (DEPLOY.md)
- Add .gitignore file
```

---

## ✅ بعد الرفع

بعد رفع التحديثات بنجاح:

1. ✅ **افتح repository على GitHub** - ستجد جميع الملفات الجديدة
2. ✅ **Render سيكتشف التحديثات تلقائياً** (إذا كان متصل بالـ repository)
3. ✅ **سيتم إعادة بناء التطبيق** على Render تلقائياً

---

## 🚀 الخطوة التالية

بعد رفع التحديثات إلى GitHub:

1. **اذهب إلى Render dashboard**
2. **تحقق من أن التطبيق يعيد البناء تلقائياً**
3. **انتظر حتى يكتمل البناء**
4. **اختبر التطبيق** على الرابط الجديد

---

**ملاحظة:** إذا لم يكن Git مثبتاً على جهازك، يمكنك:
- تثبيت Git من [git-scm.com](https://git-scm.com/)
- أو استخدام GitHub Desktop
- أو استخدام VS Code مع Git extension

