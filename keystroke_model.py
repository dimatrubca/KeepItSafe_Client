import logging
from model.keystroke_dynamics_model import predicts

logger = logging.getLogger(__name__)

def validate_user(press_timestamps, release_timestamps):
    logger.info('Validating user...')
    logger.info(str(press_timestamps))
    logger.info(str(release_timestamps))

    return predicts(press_timestamps, release_timestamps)