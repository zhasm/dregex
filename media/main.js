$(document).ready(function() {
   
    //Tabs
    $('#tabs').tabs();
    $('#useZone').tabs();

    //hover states on the static widgets
    $('#dialog_link, ul#icons li').hover(
        function() { $(this).addClass('ui-state-hover'); }, 
        function() { $(this).removeClass('ui-state-hover'); }
    );
    
    
    //textarea changes
    function text_change(item)
    {
        //actually, we need not post data frequently, instead, we can store
        //data in cache, to save bandwidth and speedup response time
        if (item)
        {
            var name=$(item).attr("name");
            var value=$(item).val();
            $.post("/text/", {name:name, value:value}, function(data){
                $("#result").html(data);
                });
        }
        //an empty update, for option change
        else{
            $.get("/text/", function(data){
                $("#result").html(data);
                });            
        }
    }
    
    //general option post 
    function option(name,value)
    {
        url="/option/"+name+"/"+value+"/";
        $.get(url);
        text_change(0);
    }
    
    //now the functions are ready, it's time to trigger them.
    
    //all regex are the same. when one place changes, other do the same.
    $(".regex").change(function(){
        var value=$(this).val();
        $(".regex").val(value);
    });
    
    
    //when text in (regex|replace|text) modified, post to the CGI.
    $(".regex, #replace, #text").keyup(function(){
        text_change(this);
        });
    
    //change the regex options
    $(".flag").click(function(){
        var name=$(this).attr("name");
        var checked=$(this).attr("checked");
        option(name, checked);
        });


        
    //tab changed; so, match:replace:split changed
    $( "#tabs" ).bind( "tabsshow", function(event, ui) {
        var sel= $( this ).tabs( "option", "selected" );
        option("action", sel);
    });
    
    
    $( "#tabs" ).bind( "tabsshow", function(event, ui) {
        var sel= $( this ).tabs( "option", "selected" );
        option("action", sel);
    });
    
    //notify the CGI that the language has been changed 
    $("#langs").change(function(){
        var lang=$(this).val();
        option("lang", lang);
        });
    $("#langs").change();
});