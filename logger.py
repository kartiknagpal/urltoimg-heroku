import logging
# create logger
lgr = logging.getLogger("url2img")
lgr.setLevel(logging.DEBUG)
# add a file handler
fh = logging.FileHandler('url2img.log')
# create a formatter and set the formatter for the handler.
frmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(frmt)
# add the Handler to the logger
lgr.addHandler(fh)