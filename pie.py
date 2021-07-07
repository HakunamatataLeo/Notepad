from pyecharts import options as opts
from pyecharts.charts import Pie, Timeline
from pyecharts.faker import Faker

# attr = Faker.choose()
tl = Timeline()
# print([list(z) for z in zip(attr, Faker.values())])
lz = {2015:[['IM', 98],
      ['话题', 48], 
      ['稿件', 103]],
      2016:[['IM', 198],
      ['话题', 48], 
      ['稿件', 81], 
      ['频道', 103]],
      2017:[['IM', 98],
      ['话题', 48], 
      ['稿件', 181], 
      ['频道', 51], 
      ['投票', 103]],
      2018:[['IM', 98],
      ['话题', 48], 
      ['稿件', 81], 
      ['频道', 152], 
      ['投票', 51], 
      ['抽奖', 103]],
      2019:[['IM', 98],
      ['话题', 48], 
      ['稿件', 81], 
      ['频道', 152], 
      ['投票', 51], 
      ['抽奖', 103], 
      ['预约', 140]],
      2020:[['IM', 98],
      ['话题', 148], 
      ['稿件', 81], 
      ['频道', 181], 
      ['投票', 151], 
      ['抽奖', 152], 
      ['预约', 140]]}
for i in range(2015, 2021):
    pie = (
        Pie()
        .add(
            "",
            lz[i],
            # [list(z) for z in zip(attr, Faker.values())],
            rosetype="radius",
            radius=["30%", "50%"],
        )
        .set_global_opts(title_opts=opts.TitleOpts("{}年xx业务".format(i)))
    )
    tl.add(pie, "{}年".format(i))
tl.render("timeline_pie.html")
