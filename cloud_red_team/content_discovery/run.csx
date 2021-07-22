#r "Newtonsoft.Json"

using System.Net;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Primitives;
using Newtonsoft.Json;

public static async Task<IActionResult> Run(HttpRequest req, ILogger log)
{
    log.LogInformation("C# HTTP trigger function processed a request.");

    string name = req.Query["name"];

    string requestBody = await new StreamReader(req.Body).ReadToEndAsync();
    dynamic data = JsonConvert.DeserializeObject(requestBody);
    name = name ?? data?.name;

    // ### User Set Variables ###
    string urlToTest = "http://opback.com/";
    string wordlistToTest = "quickhits_noslash_short.txt";
    string nameOfThisAzureFunction = "HttpTrigger010";
    // ### Setup Var to Return From API ###
    var apiReturnString = string.Empty;
    apiReturnString = apiReturnString + System.Environment.NewLine;
    // ### Execute Content Discovery ###
    var lines = File.ReadLines("D:\\home\\site\\wwwroot\\" + nameOfThisAzureFunction + "\\" + wordlistToTest);
    foreach (var line in lines) {
        var response = string.Empty;
        string urlToTry = urlToTest + line;
        try
        {
            HttpResponseMessage result = await client.GetAsync(urlToTry);
            string urlTryAndResponse = urlToTry + " ( Status: " + result.StatusCode + " )";
            log.LogInformation(urlTryAndResponse);
            apiReturnString = apiReturnString + urlTryAndResponse + System.Environment.NewLine;
            if (result.IsSuccessStatusCode)
            {
                response = await result.Content.ReadAsStringAsync();
                log.LogInformation("response: " + response);
                apiReturnString = apiReturnString + "response: " + response + System.Environment.NewLine;
            }
        }
        catch(HttpRequestException e) 
        {
            log.LogInformation("\nException Caught!");
            log.LogInformation("Message :{0} ",e.Message);
        }
    }
    // ### ### ###

    string responseMessage = string.IsNullOrEmpty(name)
        ? "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response." + apiReturnString
                : $"Hello, {name}. This HTTP triggered function executed successfully.";

            return new OkObjectResult(responseMessage);
}
