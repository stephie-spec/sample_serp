# SERP API Documentation

This document describes the Search Engine Results Page (SERP) CRUD API. This is a sample API for demonstration purposes, focusing on the "Create" functionality.

## Creating a Search Result

This API endpoint allows you to create a new search result entry.

**Endpoint:**  `/serp`
**Method:**  POST
**Authentication:** None required for this PoC (consider implementing authentication for production)

### Request

The request should be a POST request with a JSON body containing the following fields:

* **title (string):** The title of the search result.
* **url (string):** The URL of the search result.
* **snippet (string):** A short description of the search result.

**Example Request:**

```json
{
  "title": "Sample Title",
  "url": "[https://www.example.com](https://www.example.com)",
  "snippet": "This is a sample search result."
}
