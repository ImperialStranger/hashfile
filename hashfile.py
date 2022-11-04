import typer
import hashlib


app = typer.Typer(help="Display or check SHA checksums")


class UnknownHashFunctionError(Exception):
    """Appears when the passed hash function is wrong"""
    pass


def getHash(content, hash_func):
    hash = None
    if hash_func == "md5":
        hash = hashlib.md5(content).hexdigest()
        return hash
    elif hash_func == "sha1":
        hash = hashlib.sha1(content).hexdigest()
        return hash
    elif hash_func == "sha224":
        hash = hashlib.sha224(content).hexdigest()
        return hash
    elif hash_func == "sha256":
        hash = hashlib.sha256(content).hexdigest()
        return hash
    elif hash_func == "sha384":
        hash = hashlib.sha384(content).hexdigest()
        return hash
    else:
        raise UnknownHashFunctionError(f"Unknown hash function {hash_func}")


@app.command()
def get_hash(hash_func: str = typer.Option(..., help="Specify a hash function. Such as md5, sha1, sha256"), filepath: str = typer.Option(..., help="Specify a file name or it's path")):
    """Returns the hash of a file."""
    file = open(filepath, 'rb')
    buff = file.read()
    hash = getHash(buff, hash_func)
    typer.echo(hash)


@app.command()
def verify(hash_func: str = typer.Option(..., help="Specify a hash function. Such as md5, sha1, sha256"), filepath: str = typer.Option(..., help="Specify a file name or it's path"), hash: str = typer.Option(..., help="Pass the hash to verify")):
    """Checks file itegrity."""
    file = open(filepath, 'rb')
    buff = file.read()
    sample_hash = getHash(buff, hash_func)
    if hash == sample_hash:
        typer.echo(typer.style("OK", fg=typer.colors.BRIGHT_GREEN))
    else:
        typer.echo(typer.style("NOT GOOD", fg=typer.colors.BRIGHT_RED))


if __name__ == "__main__":
    app()
