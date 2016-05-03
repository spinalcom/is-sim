from concat_js import *


models = []
views = []
stylesheets = []

for p in os.listdir( "modules" ):
    for m in os.listdir("modules/" + p):
	if m == "models":
	    models.append("gen/" + m + "/" + p + ".js")
            concat_js( "modules/" + p + "/" + m, "gen/" + m + "/" + p + ".js", "gen/stylesheets/" + p + ".css" )

	elif m == "views":
	    views.append("gen/" + m + "/" + p + ".js")
            concat_js( "modules/" + p + "/" + m, "gen/" + m + "/" + p + ".js", "gen/stylesheets/" + p + ".css" )

	elif m == "stylesheets":
	    stylesheets.append("gen/" + m + "/" + p + ".css")
            concat_js( "modules/" + p + "/" + m, "gen/" + m + "/" + p + ".js", "gen/stylesheets/" + p + ".css" )

    #for r in get_files( "modules/" + p ):
     #   print r.name
      #  if r.name.endswith( ".html" ):
       #     exec_cmd( "cp " + r.name + " ." )


exec_cmd( "echo > is-sim.models.js " )
exec_cmd( "echo > is-sim.views.js " )
exec_cmd( "echo > is-sim.stylesheets.css " )

for m in sorted(models):
    exec_cmd( "cat is-sim.models.js " + m + " > is-sim.models_tmp.js" )
    exec_cmd( "mv is-sim.models_tmp.js is-sim.models.js" )
    #exec_cmd( "mkdir -p min; slimit -m < gen/" + o + " > min/" + o )
for v in sorted(views):
    exec_cmd( "cat is-sim.views.js " + v + " > is-sim.views_tmp.js" )
    exec_cmd( "mv is-sim.views_tmp.js is-sim.views.js" )
for s in sorted(stylesheets):
    exec_cmd( "cat is-sim.stylesheets.css " + s + " > is-sim.stylesheets_tmp.css" )
    exec_cmd( "mv is-sim.stylesheets_tmp.css is-sim.stylesheets.css" )



