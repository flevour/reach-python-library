import json


def mock_request_assert_called_with(
        instance,
        mock_request,
        method,
        payload,
        url,
        content_type,
        version,
        encoding
):
    _, args, _ = mock_request.mock_calls[0]
    called_method, called_payload, called_url, called_content_type, called_version, called_encoding = args
    instance.assertEqual(method, called_method)
    if payload is not None:
        instance.assertEqual(payload, json.loads(called_payload))
    instance.assertEqual(url, called_url)
    instance.assertEqual(content_type, called_content_type)
    instance.assertEqual(version, called_version)
    instance.assertEqual(encoding, called_encoding)
