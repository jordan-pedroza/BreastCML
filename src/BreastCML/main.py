from model import Model
import click

@click.group()
def cli():
    pass




@click.command() 
@click.option('--config_path', default="", help='Path to the config file', required=True)
def trainmodel(config_path):
    print(config_path)
    model = Model(config_path)
    


cli.add_command(trainmodel)
if __name__ == "__main__":
    cli()
    # Model()
    #initmodel()
    print("hey world")