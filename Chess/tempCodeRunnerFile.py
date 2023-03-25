    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            clock.tick(MAX_FPS)
            p.display.flip()