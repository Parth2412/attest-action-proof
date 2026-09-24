"""Proof fixture: importing repository content must fail the run."""
raise RuntimeError("repository-controlled sitecustomize.py executed")
