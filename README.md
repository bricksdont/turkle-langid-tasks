# turkle-langid-tasks

Download data from rattle:

    ./scripts/download_data.sh

This will also fix some file names to be unique.

Generate tasks from the data:

    ./scripts/generate_hits.sh

With current settings, this will select 100 sentences from each system output, but will leave out most of the fine-tuned systems.
This is because the total number of systems is too high (> 100).

Instantiate worker template locally:

    ./scripts/instantiate_worker_template.sh

Then open html/worker_template.instance.html in your browser.

Our Turkle server is currently running on a development machine, forward a port to your local machine as follows:

    ssh -NT mmueller@fensalir.cli -L7000:localhost:7000