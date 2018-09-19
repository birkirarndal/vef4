<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Json py</title>
	<link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
    <%
    import json
    with open("gengi.json", "r", encoding="utf-8") as skra:
        gengi = json.load(skra)
    end
    %>
	%include('haus.tpl')

	<div class="row">
		<!--section><img src="/static/mynd0.jpg"></section-->
		<section>
		    <h2>gengi gjaldmiðla</h2>
			<ul>
				% for i in gengi['results']:
					<li>{{i['longName']}} - {{i['shortName']}} ISKR: {{i['value']}}</li>
				% end
			</ul>
		</section>
	</div>

</body>
</html>