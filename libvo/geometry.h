/* This file (C) Mark Zealey <mark@zealos.org 2002, released under GPL */
#ifndef __GEOMETRY_H
#define __GEOMETRY_H

extern char *vo_geometry;
int geometryFull(int *pwidth, int *pheight, int *xpos, int *ypos, int scrw, int scrh, int vidw, int vidh);
int geometry(int *xpos, int *ypos, int scrw, int scrh, int vidw, int vidh);

#endif /* !__GEOMETRY_H */
