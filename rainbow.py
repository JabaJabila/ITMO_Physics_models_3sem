from vpython import *

scene = canvas(
    background=vec(1, 1, 1),
    width=1200,
    height=600,
    center=vec(0, 0, 0),
    range=120,
    forward=vec(1, -1, -2),
    userspin=False,
    userpan=False,
    userzoom=True,
    caption='',
)

earth = box(size=vec(1000, 1, 1000), color=color.green, opacity=0.8)
observer = sphere(pos=vec(0, 0, 0), radius=5, color=color.blue)
observer_label = label(pos=observer.pos,
                       text='наблюдатель',
                       xoffset=-30,
                       yoffset=30,
                       box=False)

main_axis = cylinder(pos=observer.pos,
                     color=color.black,
                     radius=1,
                     axis=vec(200, 0, 0))

anti_axis = cylinder(pos=observer.pos,
                     color=color.black,
                     radius=1,
                     axis=-main_axis.axis)
_thickness = 1

_rainbow = [
    ring(pos=main_axis.axis / 2,
         axis=main_axis.axis,
         radius=mag(main_axis.axis / 2) * tan(42 * pi / 180),
         thickness=_thickness,
         color=color.red),

    ring(pos=main_axis.axis / 2,
         axis=main_axis.axis,
         radius=mag(main_axis.axis / 2) * tan(41.8 * pi / 180),
         thickness=_thickness,
         color=color.orange),

    ring(pos=main_axis.axis / 2,
         axis=main_axis.axis,
         radius=mag(main_axis.axis / 2) * tan(41.2 * pi / 180),
         thickness=_thickness,
         color=color.yellow),

    ring(pos=main_axis.axis / 2,
         axis=main_axis.axis,
         radius=mag(main_axis.axis / 2) * tan(40.8 * pi / 180),
         thickness=_thickness,
         color=color.green),

    ring(pos=main_axis.axis / 2,
         axis=main_axis.axis,
         radius=mag(main_axis.axis / 2) * tan(40.4 * pi / 180),
         thickness=_thickness / 2,
         color=color.cyan),

    ring(pos=main_axis.axis / 2,
         axis=main_axis.axis,
         radius=mag(main_axis.axis / 2) * tan(40.2 * pi / 180),
         thickness=_thickness / 2,
         color=color.blue),

    ring(pos=main_axis.axis / 2,
         axis=main_axis.axis,
         radius=mag(main_axis.axis / 2) * tan(40 * pi / 180),
         thickness=_thickness,
         color=color.purple)
]

sun_light = [
    cylinder(pos=_rainbow[0].pos + _rainbow[0].radius * rotate(norm(main_axis.axis), pi / 2),
             radius=0.5,
             axis=-main_axis.axis,
             color=color.white),

    cylinder(pos=_rainbow[5].pos + _rainbow[5].radius * rotate(norm(main_axis.axis), pi / 2),
             radius=0.5,
             axis=-main_axis.axis,
             color=color.white)
]

rays = [
    arrow(pos=sun_light[0].pos,
          shaftwidth=0.5,
          headwidth=2,
          axis=1 / cos(42 * pi / 180) * rotate(-main_axis.axis / 2, 42 * pi / 180),
          color=color.red),

    arrow(pos=sun_light[0].pos,
          shaftwidth=0.5,
          headwidth=2,
          axis=1 / cos(40 * pi / 180) * rotate(-main_axis.axis / 2, 40 * pi / 180),
          color=color.purple),

    arrow(pos=sun_light[1].pos,
          shaftwidth=0.5,
          headwidth=2,
          axis=1 / cos(42 * pi / 180) * rotate(-main_axis.axis / 2, 42 * pi / 180),
          color=color.red),

    arrow(pos=sun_light[1].pos,
          shaftwidth=0.5,
          headwidth=2,
          axis=1 / cos(40 * pi / 180) * rotate(-main_axis.axis / 2, 40 * pi / 180),
          color=color.purple)
]


def rotate_rainbow(my_slider):
    global main_axis, anti_axis, _rainbow, sun_light, rays

    angle = -my_slider.value
    new_axis = rotate(vec(200, 0, 0), angle)
    main_axis.axis = new_axis
    anti_axis.axis = -new_axis

    for i in range(7):
        _rainbow[i].axis = rotate(vec(200, 0, 0), angle)
        _rainbow[i].pos = rotate(vec(200, 0, 0), angle) / 2

    sun_light[0].axis = -new_axis
    sun_light[0].pos = _rainbow[0].pos + _rainbow[0].radius * rotate(norm(new_axis), pi / 2)

    sun_light[1].axis = -new_axis
    sun_light[1].pos = _rainbow[5].pos + _rainbow[5].radius * rotate(norm(new_axis), pi / 2)

    rays[0].pos = sun_light[0].pos
    rays[0].axis = 1 / cos(42 * pi / 180) * rotate(-new_axis / 2, 42 * pi / 180)

    rays[1].pos = sun_light[0].pos
    rays[1].axis = 1 / cos(40 * pi / 180) * rotate(-new_axis / 2, 40 * pi / 180)

    rays[2].pos = sun_light[1].pos
    rays[2].axis = 1 / cos(42 * pi / 180) * rotate(-new_axis / 2, 42 * pi / 180)

    rays[3].pos = sun_light[1].pos
    rays[3].axis = 1 / cos(40 * pi / 180) * rotate(-new_axis / 2, 40 * pi / 180)


def run(a_slider):
    rotate_rainbow(a_slider)
    angle_label.text = "Угол Солнца: {0:3.1f}".format(a_slider.value * 180 / pi) + " градусов"


angle_label = wtext(text='', pos=scene.title_anchor, )
angle_slider = slider(vertical=True,
                      max=pi / 2,
                      min=0,
                      bind=run,
                      align='left',
                      pos=scene.title_anchor)

run(angle_slider)
