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
	r = cname_sname[1];
	id = cname_sname[2];
	if (r == 'song') {
		$('#' + id).addClass("active");
	}
	else if (r == 'playlist'){
		$('.playlist.' + id).addClass("active");
		if(cname_sname.length > 2){
			sid = cname_sname[4]
			console.log("sid:", sid);
			$('#' + sid).addClass("active");
		}
	}

}

addLoadEvent(activate);
