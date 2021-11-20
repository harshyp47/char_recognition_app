import 'package:http/http.dart' as http;

// Future GetData(url) async {
//   http.Response Response = await http.get(url);

//   return Response.body;
// }

Future<http.Response> fetchAlbum() {
  return http.get(Uri.http('127.0.0.1:5000', 'api'));
}
