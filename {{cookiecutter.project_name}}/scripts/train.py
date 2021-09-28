
import pytorch_lightning as pl

from {{cookiecutter.project_name}} import models


parser = ArgumentParser(description="{{cookiecutter.project_name}} model training script")
parser.add_argument(
    "--epochs",
    type=int,
    default=50,
    metavar="N",
    help="number of epochs to train (default: 50)",
)
parser.add_argument(
    "--model",
    type=str,
    default="",
    help="Model specification, refer to base.py",
)
parser.add_argument(
    "--cpu", type=bool, default=False, help="Force CPU model (default: False"
)
parser.add_argument(
    "--sweep",
    type=bool,
    default=False,
    help="If using wandb for a sweep (default: False",
)
parser.add_argument("--batch_size", type=int, default=64)
parser.add_argument("--dataset", type=str, default="devset.h5")
parser.add_argument("--clip", type=float, default=0.)
# this grabs the model choice without running parse_args
temp_args, _ = parser.parse_known_args()
# pick out the model we want to train
model_choice = models.get(temp_args.model)

logger = pl.loggers.TensorBoardLogger()
