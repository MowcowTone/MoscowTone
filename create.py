class generat():
    def squares(x,y,start_x,start_y):
        squares = []
        for j in range(x):
            for i in range(y):
                squares.append([
                    [(start_x+0.03)+j*0.030, (start_y+0.015)-i*0.015],
                    [(start_x+0.03)+j*0.030, start_y-i*0.015],
                    [start_x+j*0.030, start_y-i*0.015],
                    [start_x+j*0.030, (start_y+0.015)-i*0.015]
                ])
        return squares
    def postomsts(shag,start_x,start_y,cvadrat):
        post = []
        for k in range(cvadrat):
            for c in range(cvadrat):
                for i in range(shag):
                    for j in range(shag):
                        sh =0.03/(shag+1)
                        sg = 0.015/(shag+1)
                        post.append([round(((start_x)+((i+1)*sh)+(c*0.03)),5),round(((start_y)+((j+1)*sg)-(k*0.015)),5)])
        return post