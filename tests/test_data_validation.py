{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d63733b8-b9bb-4136-8ef2-d41ab0b8561b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pytest\n",
    "from src.data_validation import load_data, validate_schema, validate_no_nulls\n",
    "\n",
    "@pytest.fixture\n",
    "def iris_df(tmp_path):\n",
    "    # copy iris.csv into tmp and load\n",
    "    data_file = tmp_path / \"iris.csv\"\n",
    "    data_file.write_bytes(open(\"data/iris.csv\",\"rb\").read())\n",
    "    return load_data(str(data_file))\n",
    "\n",
    "def test_schema(iris_df):\n",
    "    assert validate_schema(iris_df), \"DataFrame schema does not match expected IRIS columns.\"\n",
    "\n",
    "def test_no_nulls(iris_df):\n",
    "    assert validate_no_nulls(iris_df), \"Found nulls in the DataFrame.\"\n"
   ]
  }
 ],
 "metadata": {
  "environment": {
   "kernel": "conda-base-py",
   "name": "workbench-notebooks.m130",
   "type": "gcloud",
   "uri": "us-docker.pkg.dev/deeplearning-platform-release/gcr.io/workbench-notebooks:m130"
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel) (Local)",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
