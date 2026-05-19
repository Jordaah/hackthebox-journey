<template>
	<nav>
		<router-link to="/">Home</router-link> |
		<router-link to="/try">Try our model</router-link> |
		<router-link to="/dashboard">Alien dashboard</router-link>
	</nav>
	<router-view/>
</template>

<script>
	var link = document.querySelector("link[rel*='icon']") || document.createElement('link');
	link.type = 'image/x-icon';
	link.rel = 'shortcut icon';
	link.href = require(`@/assets/img/thunder.png`);
	document.getElementsByTagName('head')[0].appendChild(link);
</script>

<style>
@import url('https://fonts.cdnfonts.com/css/aux-dotbitc');

html {
	height: 100%;
}

body {
	background-image: url('~@/assets/img/sky.jpg');
	background-repeat: repeat;
	height: 100%;
	background-position: center;
	background-size: cover;
}

#app {
	font-family: 'AuX DotBitC', sans-serif;
	text-align: center;
	color: #2c3e50;
}

nav {
	width: 90%;
	padding-top: 30px;
	padding-bottom: 30px;
	margin-right: 5%;
	margin-left: 5%;
}

nav a {
	font-size: 1.2em;
	font-weight: bold;
	color: white;
}

nav a.router-link-exact-active {
	color: #DE58D1;
}
</style>
