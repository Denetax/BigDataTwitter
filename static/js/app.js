/**
 * Created by Mehdi on 19/05/2016.
 */

$(document).ready(function() {
    $('#InfoGfi').DataTable();
    $('#InfoGfiFollowers').DataTable();
    $('#InfoGfiPays').DataTable();
    $('#BlockInformation').DataTable({
        "paging": false,
        "searching": false
    }
    );

    $( "#TopTweet" ).click(function() {
        $("#TopTweet").attr("class","active");
        $("#TopFollowers").attr("class","");
        $("#TopPays").attr("class","");

        $("#blockTopPays").attr("style","display:none;");
        $("#blockTopFollowers").attr("style","display:none;");
        $("#blockTopTweet").attr("style","display:inline;");
    });

    $( "#TopFollowers" ).click(function() {
        $("#TopFollowers").attr("class","active");
        $("#TopTweet").attr("class","");
        $("#TopPays").attr("class","");

        $("#blockTopPays").attr("style","display:none;");
        $("#blockTopTweet").attr("style","display:none;");
        $("#blockTopFollowers").attr("style","display:inline;");
    });

     $( "#TopPays" ).click(function() {
        $("#TopPays").attr("class","active");
        $("#TopTweet").attr("class","");
        $("#TopFollowers").attr("class","");

        $("#blockTopTweet").attr("style","display:none;");
        $("#blockTopFollowers").attr("style","display:none;");
        $("#blockTopPays").attr("style","display:inline;");
    });
} );
