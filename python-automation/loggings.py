import logging

logging.basicConfig(
    filename="app.log" ,
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
    )

logging.debug("checkimng been grinder RPMs")
logging.info("order #123 completed")
logging.warning("Low milk supply")
logging.error("Frother Malfuctioning")
logging.critical("Power outrage! closing shop. ")

