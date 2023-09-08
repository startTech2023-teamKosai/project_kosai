import http.requests.*;
String apiUrl = "https://chat.openai.com/";
HTTPRequest request = new HTTPRequest(apiUrl);
HTTPRequest request = new HTTPRequest(apiUrl, HTTPMethod.POST);
request.setHeader("Authorization", "Bearer YOUR_API_KEY");
HTTPResponse response = request.send();

if (response != null && response.statusCode == 200) {
  String responseBody = response.getContent();
  // レスポンスデータを処理するコードを記述
} else {
  // エラーハンドリング
  println("Error: " + response.statusCode);
}
