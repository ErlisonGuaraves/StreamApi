import json

async def stream_data(data):
    """Stream JSON data as bytes."""
    yield "["  # Start of JSON array
    first = True
    for row in data:
        if not first:
            yield ","  # Separate items with a comma
        else:
            first = False
        yield json.dumps(row)
    yield "]"  # End of JSON array
