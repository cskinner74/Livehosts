# Livehosts

Tool to analyze list of URLs for live hosts. The final output organizes results by status code. Currently includes 200, 404, and 503 results. More will be added soon.

## Usage
`livehosts.py [-s] [-v] [-o outfile] input_file`

Example:
`livehosts.py -s sample_url_list`

## Options
The `-s` flag tells the script to add http:// and https:// before checking the URL, in cases where one has a domain list without the schema.

The `-v` flag enables verbose output, displaying each URL as it's found. Non-verbose mode only shows the banner and final output.

The '-o' flag writes the final output to a file, ex: `-o outfile.txt`
## TODO
- ~~Add option to output to file~~
