
# Web Server in Flask

A web server built in flask to expose an endpoint in the format : [GET]<example.com>/api/hello?visitor_name="Mark" (where<example.com>is the server origin)

## API Reference

#### Get IP location and temperature

```http
  GET /api/hello?visitor_name="Mark"
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`



