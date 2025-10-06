from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trung Thu 2025 - Nhà Sò A6 🏮</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&family=Pacifico&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Quicksand', sans-serif;
            overflow-x: hidden;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            min-height: 100vh;
            color: #f8f9fa;
            position: relative;
        }
        
        /* Animated Background */
        .stars {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
        }
        
        .star {
            position: absolute;
            width: 2px;
            height: 2px;
            background: #fff;
            border-radius: 50%;
            animation: twinkle 3s infinite;
        }
        
        @keyframes twinkle {
            0%, 100% { opacity: 0.3; transform: scale(1); }
            50% { opacity: 1; transform: scale(1.5); }
        }
        
        .cloud {
            position: fixed;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 100px;
            animation: float 30s infinite linear;
            pointer-events: none;
            z-index: 1;
        }
        
        @keyframes float {
            from { transform: translateX(-200px); }
            to { transform: translateX(100vw); }
        }
        
        /* Lanterns */
        .lantern {
            position: fixed;
            width: 60px;
            height: 80px;
            z-index: 2;
            animation: swing 3s ease-in-out infinite;
            pointer-events: none;
        }
        
        .lantern-body {
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #ff6b6b, #ff8e53);
            border-radius: 10px;
            position: relative;
            box-shadow: 0 0 20px rgba(255, 107, 107, 0.6);
        }
        
        .lantern-top, .lantern-bottom {
            width: 100%;
            height: 8px;
            background: #8b4513;
            position: absolute;
            left: 0;
        }
        
        .lantern-top { top: -8px; border-radius: 10px 10px 0 0; }
        .lantern-bottom { bottom: -8px; border-radius: 0 0 10px 10px; }
        
        @keyframes swing {
            0%, 100% { transform: rotate(-5deg); }
            50% { transform: rotate(5deg); }
        }
        
        /* Main Container */
        .container {
            position: relative;
            z-index: 10;
            display: flex;
            min-height: 100vh;
            padding: 40px;
            gap: 20px;
            align-items: center;
        }
        
        /* Left Section - Wishes */
        .left-section {
            flex: 4;
            display: flex;
            flex-direction: column;
            gap: 30px;
        }
        
        .header {
            text-align: center;
            padding: 20px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .header h1 {
            font-family: 'Pacifico', cursive;
            font-size: 3em;
            background: linear-gradient(135deg, #ffd700, #ffa500);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 0 0 30px rgba(255, 215, 0, 0.3);
            margin-bottom: 10px;
        }
        
        .wishes-card {
            background: rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 40px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }
        
        .wishes-card h2 {
            font-size: 2em;
            color: #ffd700;
            margin-bottom: 20px;
            text-align: center;
        }
        
        .wish-text {
            font-size: 1.2em;
            line-height: 1.8;
            color: #f8f9fa;
            text-align: justify;
        }
        
        /* Center Section - Mooncake */
        .center-section {
            flex: 2;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .mooncake-container {
            position: relative;
            cursor: pointer;
            transition: transform 0.3s ease;
        }
        
        .mooncake-container:hover {
            transform: scale(1.15) rotate(5deg);
        }
        
        .mooncake-container:active {
            transform: scale(0.95) rotate(-5deg);
        }
        
        .mooncake {
            width: 180px;
            height: 180px;
            background: linear-gradient(135deg, #f4a460 0%, #d2691e 100%);
            border-radius: 50%;
            position: relative;
            box-shadow: 0 0 40px rgba(244, 164, 96, 0.6),
                        inset 0 0 20px rgba(0, 0, 0, 0.2);
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { box-shadow: 0 0 40px rgba(244, 164, 96, 0.6), inset 0 0 20px rgba(0, 0, 0, 0.2); }
            50% { box-shadow: 0 0 60px rgba(244, 164, 96, 0.9), inset 0 0 20px rgba(0, 0, 0, 0.2); }
        }
        
        .mooncake::before {
            content: '福';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 4em;
            font-weight: bold;
            color: #8b4513;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        
        /* Right Section - Photos */
        .right-section {
            flex: 4;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        .photo-tabs {
            display: flex;
            gap: 10px;
            justify-content: center;
            background: rgba(255, 255, 255, 0.05);
            padding: 15px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }
        
        .tab-btn {
            padding: 12px 24px;
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid rgba(255, 215, 0, 0.3);
            border-radius: 10px;
            color: #ffd700;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: 'Quicksand', sans-serif;
            font-weight: 600;
            font-size: 1em;
        }
        
        .tab-btn:hover {
            background: rgba(255, 215, 0, 0.2);
            transform: translateY(-2px);
        }
        
        .tab-btn.active {
            background: linear-gradient(135deg, #ffd700, #ffa500);
            color: #1a1a2e;
            border-color: #ffd700;
        }
        
        .photo-container {
            background: rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 30px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            min-height: 500px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        /* Slideshow Mode */
        .slideshow {
            width: 100%;
            height: 100%;
            position: relative;
            display: none;
        }
        
        .slideshow.active {
            display: block;
        }
        
        .slide {
            display: none;
            width: 100%;
            height: 450px;
            position: relative;
        }
        
        .slide.active {
            display: flex;
            justify-content: center;
            align-items: center;
            animation: fadeIn 0.5s ease;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: scale(0.95); }
            to { opacity: 1; transform: scale(1); }
        }
        
        .slide img {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        }
        
        /* Grid Mode */
        .grid-view {
            display: none;
            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            gap: 15px;
            max-height: 500px;
            overflow-y: auto;
            padding-right: 10px;
        }
        
        .grid-view.active {
            display: grid;
        }
        
        .grid-view::-webkit-scrollbar {
            width: 8px;
        }
        
        .grid-view::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
        }
        
        .grid-view::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #ffd700, #ffa500);
            border-radius: 10px;
        }
        
        .grid-item {
            position: relative;
            overflow: hidden;
            border-radius: 10px;
            cursor: pointer;
            transition: transform 0.3s ease;
            aspect-ratio: 1;
        }
        
        .grid-item:hover {
            transform: scale(1.05);
            z-index: 10;
        }
        
        .grid-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }
        
        /* Manual Mode */
        .manual-view {
            display: none;
            width: 100%;
            height: 100%;
            position: relative;
        }
        
        .manual-view.active {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
        }
        
        .manual-image {
            width: 100%;
            height: 400px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .manual-image img {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        }
        
        .manual-controls {
            display: flex;
            gap: 15px;
            align-items: center;
        }
        
        .nav-btn {
            padding: 12px 24px;
            background: linear-gradient(135deg, #ffd700, #ffa500);
            border: none;
            border-radius: 10px;
            color: #1a1a2e;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 1em;
        }
        
        .nav-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(255, 215, 0, 0.5);
        }
        
        .image-counter {
            font-size: 1.1em;
            color: #ffd700;
            font-weight: 600;
        }
        
        /* Popup Modal */
        .modal {
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(10px);
            animation: fadeIn 0.3s ease;
        }
        
        .modal.active {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .modal-content {
            background: linear-gradient(135deg, rgba(255, 215, 0, 0.15), rgba(255, 165, 0, 0.15));
            backdrop-filter: blur(20px);
            border: 2px solid rgba(255, 215, 0, 0.5);
            border-radius: 30px;
            padding: 50px;
            max-width: 600px;
            text-align: center;
            position: relative;
            animation: scaleIn 0.3s ease;
            box-shadow: 0 0 100px rgba(255, 215, 0, 0.3);
        }
        
        @keyframes scaleIn {
            from { transform: scale(0.8); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
        }
        
        .modal-content h2 {
            font-family: 'Pacifico', cursive;
            font-size: 2.5em;
            background: linear-gradient(135deg, #ffd700, #ffa500);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 20px;
            line-height: 1.5;
        }
        
        .close-btn {
            position: absolute;
            top: 20px;
            right: 30px;
            font-size: 2em;
            color: #ffd700;
            cursor: pointer;
            transition: transform 0.3s ease;
        }
        
        .close-btn:hover {
            transform: rotate(90deg) scale(1.2);
        }
        
        /* Cursor Effect */
        * {
            cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><circle cx="16" cy="16" r="8" fill="%23ffd700" opacity="0.5"/><circle cx="16" cy="16" r="4" fill="%23ffa500"/></svg>') 16 16, auto;
        }
        
        a, button, .mooncake-container, .grid-item, .tab-btn, .nav-btn {
            cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><circle cx="16" cy="16" r="10" fill="%23ffd700" opacity="0.8"/><circle cx="16" cy="16" r="6" fill="%23ff6b6b"/></svg>') 16 16, pointer !important;
        }
        
        /* Click Ripple Effect */
        .ripple {
            position: fixed;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(255, 215, 0, 0.6) 0%, rgba(255, 165, 0, 0.3) 50%, transparent 100%);
            pointer-events: none;
            animation: rippleEffect 0.8s ease-out;
            z-index: 9999;
        }
        
        @keyframes rippleEffect {
            from {
                width: 0;
                height: 0;
                opacity: 1;
            }
            to {
                width: 200px;
                height: 200px;
                opacity: 0;
            }
        }
        
        /* Click Here Hint */
        .click-hint {
            position: absolute;
            bottom: -80px;
            left: 50%;
            transform: translateX(-50%);
            background: linear-gradient(135deg, #ff6b6b, #ffa500);
            color: white;
            padding: 12px 24px;
            border-radius: 25px;
            font-family: 'Pacifico', cursive;
            font-size: 1.2em;
            box-shadow: 0 5px 25px rgba(255, 107, 107, 0.5);
            animation: bounce 2s infinite, glow 1.5s infinite;
            white-space: nowrap;
            z-index: 100;
        }
        
        .click-hint::before {
            content: '👆';
            position: absolute;
            top: -30px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 2em;
            animation: pointUp 1s infinite;
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateX(-50%) translateY(0); }
            50% { transform: translateX(-50%) translateY(-10px); }
        }
        
        @keyframes pointUp {
            0%, 100% { transform: translateX(-50%) translateY(0); }
            50% { transform: translateX(-50%) translateY(-5px); }
        }
        
        @keyframes glow {
            0%, 100% { box-shadow: 0 5px 25px rgba(255, 107, 107, 0.5); }
            50% { box-shadow: 0 5px 40px rgba(255, 165, 0, 0.8); }
        }
        
        .click-hint.hidden {
            display: none;
        }
        
        /* Responsive */
        @media (max-width: 1200px) {
            .container {
                flex-direction: column;
                padding: 20px;
            }
            
            .left-section, .right-section {
                width: 100%;
            }
            
            .header h1 {
                font-size: 2em;
            }
        }
    </style>
</head>
<body>
    <!-- Background Elements -->
    <div class="stars" id="stars"></div>
    
    <!-- Lanterns -->
    <div class="lantern" style="top: 50px; left: 10%;">
        <div class="lantern-top"></div>
        <div class="lantern-body"></div>
        <div class="lantern-bottom"></div>
    </div>
    <div class="lantern" style="top: 100px; right: 15%; animation-delay: -1s;">
        <div class="lantern-top"></div>
        <div class="lantern-body"></div>
        <div class="lantern-bottom"></div>
    </div>
    
    <!-- Main Container -->
    <div class="container">
        <!-- Left Section -->
        <div class="left-section">
            <div class="header">
                <h1>🏮 Trung Thu 2025 🏮</h1>
                <p style="font-size: 1.2em; color: #ffa500;">Nhà Sò A6</p>
            </div>
            
            <div class="wishes-card">
                <h2>💫 Lời Chúc 💫</h2>
                <div class="wish-text">
                    <p style="margin-bottom: 15px;">
                        Trung thu đến rồi, ánh trăng sáng ngời, lòng ta rộn ràng niềm vui. 
                        Được ở bên nhau, cùng nhau lớn lên, là điều hạnh phúc nhất!
                    </p>
                    <p style="margin-bottom: 15px;">
                        Chúc cả nhà Sò A6 luôn vui vẻ, khỏe mạnh, học giỏi chơi khỏe. 
                        Mỗi ngày là một niềm vui mới, mỗi khoảnh khắc đều đáng nhớ.
                    </p>
                    <p style="margin-bottom: 15px;">
                        Dù mai sau có đi về đâu, kỷ niệm về những ngày tháng bên nhau 
                        sẽ mãi là món quà quý giá nhất trong lòng mỗi người.
                    </p>
                    <p style="text-align: center; font-size: 1.3em; color: #ffd700; font-weight: 700; margin-top: 20px;">
                        Chúc mừng Trung Thu! 🌕✨
                    </p>
                </div>
            </div>
        </div>
        
        <!-- Center Section -->
        <div class="center-section">
            <div class="mooncake-container" onclick="openModal()">
                <div class="mooncake"></div>
                <div class="click-hint" id="clickHint">Click vào ik! 🥮</div>
            </div>
        </div>
        
        <!-- Right Section -->
        <div class="right-section">
            <div class="photo-tabs">
                <button class="tab-btn active" onclick="switchTab('slideshow')">📽️ Slideshow</button>
                <button class="tab-btn" onclick="switchTab('grid')">🖼️ Grid</button>
                <button class="tab-btn" onclick="switchTab('manual')">👆 Manual</button>
            </div>
            
            <div class="photo-container">
                <!-- Slideshow -->
                <div class="slideshow active" id="slideshow">
                    {% for img in images %}
                    <div class="slide {% if loop.first %}active{% endif %}">
                        <img src="{{ url_for('serve_image', filename=img) }}" alt="Ảnh {{ loop.index }}">
                    </div>
                    {% endfor %}
                </div>
                
                <!-- Grid View -->
                <div class="grid-view" id="grid">
                    {% for img in images %}
                    <div class="grid-item" onclick="viewImage({{ loop.index0 }})">
                        <img src="{{ url_for('serve_image', filename=img) }}" alt="Ảnh {{ loop.index }}">
                    </div>
                    {% endfor %}
                </div>
                
                <!-- Manual View -->
                <div class="manual-view" id="manual">
                    <div class="manual-image">
                        <img id="manualImg" src="" alt="Ảnh">
                    </div>
                    <div class="manual-controls">
                        <button class="nav-btn" onclick="prevImage()">◀ Trước</button>
                        <span class="image-counter" id="counter">1 / {{ images|length }}</span>
                        <button class="nav-btn" onclick="nextImage()">Sau ▶</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Modal -->
    <div class="modal" id="modal">
        <div class="modal-content">
            <span class="close-btn" onclick="closeModal()">×</span>
            <h2>Chúc cả nhà A6<br>Trung Thu dui dẻ nháaa 🥮🌕</h2>
        </div>
    </div>
    
    <audio id="bgMusic" loop autoplay>
        <source src="{{ url_for('serve_music') }}" type="audio/mpeg">
    </audio>
    
    <script>
        // Click ripple effect
        document.addEventListener('click', function(e) {
            const ripple = document.createElement('div');
            ripple.className = 'ripple';
            ripple.style.left = (e.clientX - 100) + 'px';
            ripple.style.top = (e.clientY - 100) + 'px';
            document.body.appendChild(ripple);
            
            setTimeout(() => ripple.remove(), 800);
        });
        
        // Auto-play music with user interaction fallback
        const music = document.getElementById('bgMusic');
        
        // Try to play immediately
        music.play().catch(() => {
            // If autoplay is blocked, play on first user interaction
            document.addEventListener('click', function playOnce() {
                music.play();
                document.removeEventListener('click', playOnce);
            }, { once: true });
        });
        
        // Generate stars
        const starsContainer = document.getElementById('stars');
        for (let i = 0; i < 100; i++) {
            const star = document.createElement('div');
            star.className = 'star';
            star.style.left = Math.random() * 100 + '%';
            star.style.top = Math.random() * 100 + '%';
            star.style.animationDelay = Math.random() * 3 + 's';
            starsContainer.appendChild(star);
        }
        
        // Generate clouds
        for (let i = 0; i < 5; i++) {
            const cloud = document.createElement('div');
            cloud.className = 'cloud';
            cloud.style.width = (Math.random() * 200 + 100) + 'px';
            cloud.style.height = (Math.random() * 50 + 30) + 'px';
            cloud.style.top = Math.random() * 60 + '%';
            cloud.style.animationDuration = (Math.random() * 20 + 20) + 's';
            cloud.style.animationDelay = Math.random() * 10 + 's';
            document.body.appendChild(cloud);
        }
        
        // Slideshow
        let slideIndex = 0;
        let slideshowInterval;
        
        function showSlides() {
            const slides = document.querySelectorAll('#slideshow .slide');
            slides.forEach((slide, index) => {
                slide.classList.remove('active');
                if (index === slideIndex) {
                    slide.classList.add('active');
                }
            });
            slideIndex = (slideIndex + 1) % slides.length;
        }
        
        function startSlideshow() {
            showSlides();
            slideshowInterval = setInterval(showSlides, 3000);
        }
        
        startSlideshow();
        
        // Tab switching
        function switchTab(mode) {
            // Clear slideshow interval
            clearInterval(slideshowInterval);
            
            // Update buttons
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            
            // Update views
            document.getElementById('slideshow').classList.remove('active');
            document.getElementById('grid').classList.remove('active');
            document.getElementById('manual').classList.remove('active');
            
            if (mode === 'slideshow') {
                document.getElementById('slideshow').classList.add('active');
                slideIndex = 0;
                startSlideshow();
            } else if (mode === 'grid') {
                document.getElementById('grid').classList.add('active');
            } else if (mode === 'manual') {
                document.getElementById('manual').classList.add('active');
                showManualImage(0);
            }
        }
        
        // Manual navigation
        let currentManualIndex = 0;
        const images = {{ images|tojson }};
        
        function showManualImage(index) {
            currentManualIndex = index;
            const img = document.getElementById('manualImg');
            img.src = `/assets/anh-lop/${images[index]}`;
            document.getElementById('counter').textContent = `${index + 1} / ${images.length}`;
        }
        
        function prevImage() {
            currentManualIndex = (currentManualIndex - 1 + images.length) % images.length;
            showManualImage(currentManualIndex);
        }
        
        function nextImage() {
            currentManualIndex = (currentManualIndex + 1) % images.length;
            showManualImage(currentManualIndex);
        }
        
        function viewImage(index) {
            switchTab('manual');
            showManualImage(index);
            document.querySelectorAll('.tab-btn')[2].classList.add('active');
        }
        
        // Modal
        function openModal() {
            document.getElementById('modal').classList.add('active');
            document.getElementById('clickHint').classList.add('hidden');
        }
        
        function closeModal() {
            document.getElementById('modal').classList.remove('active');
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    images_dir = os.path.join(os.path.dirname(__file__), 'assets', 'anh-lop')
    images = []
    if os.path.exists(images_dir):
        images = [f for f in os.listdir(images_dir) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template_string(HTML_TEMPLATE, images=images)

@app.route('/assets/anh-lop/<filename>')
def serve_image(filename):
    return send_from_directory(os.path.join('assets', 'anh-lop'), filename)

@app.route('/assets/music/background.mp3')
def serve_music():
    music_dir = os.path.join('assets', 'music')
    music_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
    if music_files:
        return send_from_directory(music_dir, music_files[0])
    return '', 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
