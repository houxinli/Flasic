function addLoadEvent(func) {
  var oldonload = window.onload;
  if (typeof window.onload != 'function') {
    window.onload = func;
  } else {
    window.onload = function() {
      oldonload();
      func();
    }
  }
}

function changeLyric() {
	obj = document.getElementById('lyrics');
	console.log("obj:",obj);
	old_class = obj.getAttribute("class");
	flag = obj.getAttribute("flagshow");
	console.log("flag:",flag);
	console.log("old_class:",old_class);
	if (flag == '0') {
		new_class = old_class.concat("show");
		obj.setAttribute("class", new_class);
		flag = '1';
		obj.setAttribute("flagshow", flag);
	}
	else{
		new_class = old_class.replace("show", "");
		obj.setAttribute("class", new_class);
		flag = '0';
		obj.setAttribute("flagshow", flag);
	}

}

function activate() {
	obj = document.getElementById('lyrics');
	pathname = window.location.pathname;
	cname_sname = pathname.split('/');
	cname = cname_sname[1];
	sname = cname_sname[2];
	console.log("cname: ", cname);
	console.log("sname: ", sname);
	$('.' + cname).addClass("active");
	$('#' + sname).addClass("active");
}

addLoadEvent(activate);
