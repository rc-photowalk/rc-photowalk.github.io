entry = """
						<article class="thumb">
							<a href="%s" class="image"><img src="%s" alt="" /></a>
							<h2>%s</h2>
							<p>%s</p>
						</article>
"""

page = """
<!DOCTYPE HTML>
<!--
	Multiverse by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>Rail City Photo Walk</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
	</head>
	<body class="is-preload">

		<!-- Wrapper -->
			<div id="wrapper">

				<!-- Header -->
					<header id="header">
						<h1><a href="index.html"><strong>Rail City</strong> %s</a></h1>
						<nav>
							<ul>
								<li><a href="#footer" class="icon solid fa-bars">Menu</a></li>
							</ul>
						</nav>
					</header>

				<!-- Main -->
					<div id="main">
                        %s
					</div>

				<!-- Footer -->
					<footer id="footer" class="panel">
						<div class="inner split">
							<div>
								<section>
									<h2>By prompt:</h2>
									<h4><a href="prompt_00.html">Something beautiful</a></h4>
									<h4><a href="prompt_01.html">An animal</a></h4>
									<h4><a href="prompt_02.html">A flower</a></h4>
									<h4><a href="prompt_03.html">Something with texture</a></h4>
									<h4><a href="prompt_04.html">Something that makes you happy</a></h4>
									<h4><a href="prompt_05.html">Something with lines</a></h4>
									<h4><a href="prompt_06.html">Someone laughing</a></h4>
									<h4><a href="prompt_07.html">A reflection</a></h4>
									<h4><a href="prompt_08.html">A portrait</a></h4>
									<h4><a href="prompt_09.html">A sign</a></h4>
								</section>
								<p class="copyright">
									Design: <a href="http://html5up.net">HTML5 UP</a>.
								</p>
							</div>
							<div>
								<section>
									<h2>By photographer:</h2>
									<h4><a href="photographer_00.html">Bijhan</a></h4>
									<h4><a href="photographer_01.html">Cam</a></h4>
									<h4><a href="photographer_02.html">Esther</a></h4>
									<h4><a href="photographer_03.html">Jonathan</a></h4>
									<h4><a href="photographer_04.html">Josh</a></h4>
									<h4><a href="photographer_05.html">Melanie & Nelson</a></h4>
									<h4><a href="photographer_06.html">Rachel & John</a></h4>
									<h4><a href="photographer_07.html">Shirley & Aiden</a></h4>
									<h4><a href="photographer_08.html">Victoria & William</a></h4>
									<h4><a href="photographer_09.html">YJ</a></h4>
									<h4><a href="photographer_10.html">Zach</a></h4>
								</section>
							</div>
						</div>
					</footer>

			</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.poptrox.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>
"""