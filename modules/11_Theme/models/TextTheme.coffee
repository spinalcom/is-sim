# Copyright 2015 SpinalCom  www.spinalcom.com

#
# This file is part of SpinalCore.
#
# SpinalCore is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Soda is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with Soda. If not, see <http://www.gnu.org/licenses/>.



# 
class TextTheme extends Model
    constructor: ( )  ->
        super()

    beg_ctx: ( info ) ->
        ctx = info.ctx_2d()
        ctx.canvas.width = 1000
        ctx.canvas.height = 1000
        ctx.font = "14px monospace"
        ctx.textAlign = "center"
        ctx.textBaseline = "middle"        
        ctx.clearRect 0, 0, ctx.canvas.width, ctx.canvas.height
        
    end_ctx: ( info ) ->
        
    draw_proj: ( info, proj, text, color ) ->
        ctx = info.ctx_2d()   
        ctx.fillStyle = color.to_rgba()
        ctx.fillText text, proj[0], proj[1] 
