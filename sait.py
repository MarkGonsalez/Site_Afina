# ============================================================
# 1. ПОДКЛЮЧЕНИЕ БИБЛИОТЕКИ
# ============================================================

from flask import Flask  # Flask — библиотека для создания веб-сайтов на Python.
# Она обрабатывает запросы от браузера и возвращает HTML-страницы.

# ============================================================
# 2. СОЗДАНИЕ ПРИЛОЖЕНИЯ (ОБЪЕКТА САЙТА)
# ============================================================

app = Flask(__name__)  # Создаём объект приложения.
# __name__ — это имя текущего файла. Flask использует его, чтобы знать, где искать папки с картинками и видео.

# ============================================================
# 3. ГЛАВНАЯ СТРАНИЦА (АДРЕС "/")
# ============================================================

@app.route("/")  # Декоратор привязывает функцию к адресу "/" (главная страница).
def home():
    # Возвращает HTML-код, который увидит пользователь в браузере.
    return """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">         <!-- Кодировка для поддержки русских букв и эмодзи -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  <!-- Адаптация для телефонов -->

    <style>
        /* ============================================================
           СТИЛИ ДЛЯ ВСЕЙ СТРАНИЦЫ
           ============================================================ */

        /* --- 3.1. ВИДЕО-ФОН --- */
        #bg-video {
            position: fixed;         /* Видео фиксируется на экране (не двигается при скролле) */
            right: 0;               /* Прижимаем к правому краю */
            bottom: 0;              /* Прижимаем к нижнему краю */
            min-width: 100%;        /* Ширина на весь экран */
            min-height: 100%;       /* Высота на весь экран */
            z-index: -1;            /* Отправляем видео на самый нижний слой (под текст) */
            object-fit: cover;      /* Видео растягивается, заполняя весь экран без искажений */
        }

        /* --- 3.2. ОСНОВНЫЕ НАСТРОЙКИ СТРАНИЦЫ --- */
        body {
            margin: 0;
            padding: 0;
            font-family: Comic Sans MS,  /* Шрифт текста */
            min-height: 100vh;
            overflow: hidden;                /* Убираем полосы прокрутки */
            animation: fadeIn 1.5s ease-in-out;  /* Анимация появления страницы */
        }

        /* --- 3.3. ПОЛУПРОЗРАЧНЫЙ СЛОЙ ПОВЕРХ ВИДЕО --- */
        /* Этот слой делает текст читаемым поверх видео */
        body::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(255, 248, 220, 0.5);  /* Кремовый полупрозрачный слой */
            z-index: 0;                    /* Слой между видео и текстом */
        }

        /* --- 3.4. АНИМАЦИЯ ПОЯВЛЕНИЯ --- */
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(-20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        /* --- 3.5. КОНТЕЙНЕР С ТЕКСТОМ И КНОПКАМИ --- */
        .container {
            position: relative;    /* Чтобы текст был поверх всех слоёв */
            z-index: 1;            /* Поднимаем над ::before и видео */
            text-align: center;
            padding: 50px;
            max-width: 800px;
            margin: 0 auto;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: #333;
        }

        /* --- 3.6. ЗАГОЛОВОК --- */
        h1 {
            font-family: 'Comic Sans MC';
            font-size: 52px;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);  /* Тень для читаемости */
        }

        /* --- 3.7. ТЕКСТ ПОД ЗАГОЛОВКОМ --- */
        .subtext {
            font-size: 20px;
            margin-bottom: 30px;
        }

        /* --- 3.8. КНОПКИ (ОБЩИЙ СТИЛЬ) --- */
        .btn {
            display: inline-block;
            padding: 30px 45px;


border-radius: 50px;
            text-decoration: none;
            font-size: 30px;
            transition: all 0.3s ease;
            margin: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }

        /* --- 3.9. РОЗОВАЯ КНОПКА "ПОЗНАКОМИТЬСЯ" --- */
        .btn-pink {
            background: #FF69B4;
            color: white;
            font-family: 'Franklin Gothic'
        }

        .btn-pink:hover {
            background: #FF1493;
            transform: scale(1.1);
        }

        /* --- 3.10. КНОПКА "ГАЛЕРЕЯ" (ПРОЗРАЧНАЯ) --- */
        .btn-gallery {
            background: transparent;
            color: blue;
            font-family: 'Georgia'
            font-size: 40px;
            border: 4px solid blue;
            padding: 25px 40px;
        }

        .btn-gallery:hover {
            background: #FF69B4;
            color: white;
            transform: scale(1.05);
        }

        /* --- 3.11. ССЫЛКИ В МЕНЮ --- */
        .menu-links {
            margin-top: 30px;
            font-size: 16px;
        }

        .menu-links a {
            color: #333;
            text-decoration: none;
            margin: 0 10px;
        }

        .menu-links a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

    <!-- ============================================================
         3.12. ВИДЕО-ФОН (С ТВОИМ ФАЙЛОМ)
         ============================================================ -->
    <video autoplay muted loop id="bg-video">
        <!-- autoplay — запускается автоматически -->
        <!-- muted — звук выключен (обязательно для автозапуска в браузерах) -->
        <!-- loop — видео повторяется бесконечно -->

        <!-- ВОТ ЗДЕСЬ ПРОПИСЫВАЕТСЯ НАЗВАНИЕ ВИДЕОФАЙЛА -->
        <source src="/static/Afina_video.mp4" type="video/mp4">
        <!-- Если твой файл называется иначе — замени "Afina_video.mp4" на своё имя -->
        <!-- Файл должен лежать в папке "static" -->
    </video>
<audio autoplay loop id="bg-music">
    <source src="/static/Afina_music.mp3" type="audio/mpeg">
</audio>

<div class="container">
    <h1>🐩 Добро пожаловать на сайт   знакомства с Афиной!</h1>
    <a href="/afina" class="btn btn-pink">Познакомиться с Афиной 💕</a>
    <a href="/gallery" class="btn btn-gallery">📸 Галерея</a>
        </button>
    </div>
    <script>
    var music = document.getElementById("bg-music");

    function playMusicOnFirstClick() {
        music.play();
        document.removeEventListener('click', playMusicOnFirstClick);
    }

    document.addEventListener('click', playMusicOnFirstClick);
</script>

    <div class="menu-links">
        <a href="/afina">Об Афине</a> |
        <a href="/gallery">Галерея</a>
    </div>
</div>

</body>
</html>
    """

# ============================================================
# 4. СТРАНИЦА "ОБ АФИНЕ" (АДРЕС "/afina")
# ============================================================

@app.route("/afina")
def afina():
    return """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Об Афине</title>
    <style>
    /* ============================================================
       ОБЩИЙ СТИЛЬ ДЛЯ СТРАНИЦЫ "ОБ АФИНЕ"
       ============================================================ */

    body {
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
        min-height: 100vh;
        background-image: url('/static/Afina_photo3.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        animation: fadeIn 1.5s ease-in-out;
    }

    /* ============================================================
       ПОЛУПРОЗРАЧНЫЙ СЛОЙ ДЛЯ ЧИТАЕМОСТИ ТЕКСТА
       ============================================================ */

    body::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(255, 248, 220, 0.5);
        z-index: 0;
    }

    /* ============================================================
       АНИМАЦИЯ ПОЯВЛЕНИЯ
       ============================================================ */

    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    /* ============================================================
       КОНТЕЙНЕР ДЛЯ КОНТЕНТА
       ============================================================ */

    .container {
        position: relative;
        z-index: 1;
        text-align: center;
        padding: 50px;
        max-width: 600px;
        margin: 0 auto;
    }

    /* ============================================================
       ФОТО АФИНЫ
       ============================================================ */

    .afina-photo {
        border-radius: 20px;
        border: 5px solid #FF69B4;
        width: 300px;
        transition: transform 0.3s ease;
    }

    .afina-photo:hover {
        transform: scale(1.02);
    }

    /* ============================================================
       ЗЕЛЁНАЯ КНОПКА "НА ГЛАВНУЮ"
       ============================================================ */

    .btn-green {
        background: #4CAF50;
        color: white;
        padding: 10px 20px;
        border-radius: 30px;
        text-decoration: none;
        display: inline-block;
        margin-top: 20px;
        transition: all 0.3s ease;
    }

    .btn-green:hover {
        background: #45a049;
        transform: scale(1.05);
    }
</style>
</head>
<body>
    <div class="container">
        <h1>🐩 Знакомьтесь — Афина!</h1>
        <img src="/static/Afina_photo.jpg" alt="Афина" class="afina-photo">
        <p><strong>Возраст:</strong> 6 месяцев</p>
        <p><strong>Порода:</strong> Помчи (чихуахуа + шпиц)</p>
        <p><strong>Характер:</strong> Любит спать, но если не спит — не угомонить 😄</p>
        <p><strong>Любит:</strong> валяться на кровати, грызть свои камушки и пеленку, смотреть в потолок и внезапно беситься</p>
        <a href="/" class="btn-green">⬅️ На главную</a>
    </div>
</body>
</html>
    """

# ============================================================
# 5. СТРАНИЦА "ГАЛЕРЕЯ" (АДРЕС "/gallery")
# ============================================================

@app.route("/gallery")
def gallery():
    return """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Галерея Афины</title>
    <style>
    /* ============================================================
       ОБЩИЙ СТИЛЬ ДЛЯ СТРАНИЦЫ "ГАЛЕРЕЯ"
       ============================================================ */

    body {
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
        min-height: 100vh;
        background-image: url('/static/Afina_photo4.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        animation: fadeIn 1.5s ease-in-out;
    }

    /* ============================================================
       ПОЛУПРОЗРАЧНЫЙ СЛОЙ ДЛЯ ЧИТАЕМОСТИ ТЕКСТА
       ============================================================ */

    body::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(255, 248, 220, 0.5);
        z-index: 0;
    }

    /* ============================================================
       АНИМАЦИЯ ПОЯВЛЕНИЯ
       ============================================================ */

    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    /* ============================================================
       КОНТЕЙНЕР ДЛЯ КОНТЕНТА
       ============================================================ */

    .container {
        position: relative;
        z-index: 1;
        text-align: center;
        padding: 50px;
        max-width: 1000px;
        margin: 0 auto;
    }

    /* ============================================================
       СЕТКА ДЛЯ ФОТО (FLEX)
       ============================================================ */

    .photo-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: center;
    }

    /* ============================================================
       ФОТО В ГАЛЕРЕЕ
       ============================================================ */

    .gallery-photo {
        border-radius: 40px;
        border: 5px solid #FF69B4;
        width: 280px;
        transition: transform 0.5s ease;
    }

    .gallery-photo:hover {
        transform: scale(1.9);
    }

    /* ============================================================
       ЗЕЛЁНАЯ КНОПКА "НА ГЛАВНУЮ"
       ============================================================ */

    .btn-green {
        background: #4CAF50;
        color: white;
        padding: 10px 20px;
        border-radius: 30px;
        text-decoration: none;
        display: inline-block;
        margin-top: 30px;
        transition: all 0.3s ease;
    }

    .btn-green:hover {
        background: #45a049;
        transform: scale(1.05);
    }
</style>
</head>
<body>
    <div class="container">
        <h1>📸 Галерея Афины</h1>
        <div class="photo-grid">
            <img src="/static/Afina_photo.jpg" alt="Афина" class="gallery-photo">
            <img src="/static/Afina_photo2.jpg" alt="Афина" class="gallery-photo">
            <img src="/static/Afina_photo3.jpg" alt="Афина" class="gallery-photo">
            <img src="/static/Afina_photo4.jpg" alt="Афина" class="gallery-photo">
            <img src="/static/Afina_photo6.jpg" alt="Афина" class="gallery-photo">
            <img src="/static/Afina_photo7.jpg" alt="Афина" class="gallery-photo">
        </div>
        <p style="font-size:20px;">🐩 Это наша красавица Афина! ❤️</p>
        <a href="/" class="btn-green">⬅️ На главную</a>
    </div>
</body>
</html>
    """

# ============================================================
# 6. ЗАПУСК СЕРВЕРА
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)  # Запускаем сервер с режимом отладки.