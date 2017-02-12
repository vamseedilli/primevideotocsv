from lxml import html
import urllib

page = urllib.urlopen("https://www.primevideo.com/search/ref=atv_mv_hom_c_pvacmc_6_3?_encoding=UTF8&pf_rd_i=&pf_rd_m=&pf_rd_p=&pf_rd_r=&pf_rd_s=&pf_rd_t=&query=bq%253d%28and%2520sort%3A%27featured-rank%27%2520%28and%2520av_language_spoken%3A%27IN%3Ate-in%27%2520entity_type%3A%27Movie%27%29%29")
print(page.read)
tree = html.fromstring(page.content)
print(page.content)
print(tree)