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

exec_cmd( "echo > is-sim.models.js " )
exec_cmd( "echo > is-sim.views.js " )
exec_cmd( "echo > is-sim.stylesheets.css " )

for m in sorted(models):
    exec_cmd( "cat is-sim.models.js " + m + " > is-sim.models_tmp.js" )
    exec_cmd( "mv is-sim.models_tmp.js is-sim.models.js" )
for v in sorted(views):
    exec_cmd( "cat is-sim.views.js " + v + " > is-sim.views_tmp.js" )
    exec_cmd( "mv is-sim.views_tmp.js is-sim.views.js" )
for s in sorted(stylesheets):
    exec_cmd( "cat is-sim.stylesheets.css " + s + " > is-sim.stylesheets_tmp.css" )
    exec_cmd( "mv is-sim.stylesheets_tmp.css is-sim.stylesheets.css" )

exec_cmd( "cp modules/Admin/admin.html ../../browser-organs" )
exec_cmd( "cp modules/Desk/desk.html ../../browser-organs" )
exec_cmd( "cp modules/Lab/lab.html ../../browser-organs" )