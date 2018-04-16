/* Global Variables */
var layers,
    featureOverlay,
    wmsLayer,
    wms_url,
    map,
    info,
    displayFeatureInfo,
    view,
    current_layer,
    res_name,
    coordinate,
    map_events;




/* clicking on the shapefile uses this function. We need to make it automatic instead of hardcoded*/
function goToURL() {
   location.href = 'http://127.0.0.1:8000/apps/reservoir-management/sabana-yegua/';
}

/*this function creates the base map on the home page*/
function init_map(){


    /*basemap for the map*/
    var base_layer = new ol.layer.Tile({
        source: new ol.source.BingMaps({
            key: 'eLVu8tDRPeQqmBlKAjcw~82nOqZJe2EpKmqd-kQrSmg~AocUZ43djJ-hMBHQdYDyMbT-Enfsk0mtUIGws1WeDuOvjY4EXCH-9OK3edNLDgkc',
            imagerySet: 'AerialWithLabels'
        })
    });

    /*initial view for the map. You can change the view by changing the lat,long or zoom */
    var view = new ol.View({
        center: ol.proj.transform([-71.4, 18.8], 'EPSG:4326', 'EPSG:3857'),
        minZoom: 2,
        maxZoom: 18,
        zoom:8.3
    });


    /*getting the specific parts that will be used by the popup*/
    var container = document.getElementById('popup');
    var content = document.getElementById('popup-content');
    var closer = document.getElementById('popup-closer');

    /*information for popup*/
    var overlay = new ol.Overlay({
        element: container,
        autoPan: true,
        autoPanAnimation: {
          duration: 250
        }
    });

    /*closes popup on click*/
    closer.onclick = function() {
        overlay.setPosition(undefined);
        closer.blur();
        return false;
    };

    /*identifies which layers will show in the map*/
    layers = [base_layer];

    /*creates the map with the specified views, layers, and popups from above*/
    map = new ol.Map({
        target: 'map',
        view: view,
        layers:layers,
        overlays: [overlay],
    });

    /*searched for the reservoir layer on the geoserver and grabs it. This will need to be changed when installed on a different computer*/
    var wmsLayer = new ol.layer.Image({
        source: new ol.source.ImageWMS({
            url: 'http://tethys-staging.byu.edu:8181/geoserver/wms',
            params: {'LAYERS': 'reservoirs'},
            serverType: 'geoserver',
            crossOrigin: 'Anonymous'
        })
    });
    map.addLayer(wmsLayer);


    /*these events occur when the mouse moves*/
    map.on('pointermove', function(evt) {

        var pixel = map.getEventPixel(evt.originalEvent);
        var hit = map.forEachLayerAtPixel(pixel, function(layer) {
            if (layer != layers[0] && layer != layers[1] && layer != layers[2] && layer != layers[3]){
                current_layer = layer;
                return true;}
        });

        /*when the cursor hits a shapefile, it turns into a pointer hand*/
        map.getTargetElement().style.cursor = hit ? 'pointer' : '';

        /*when the cursor is a pointer, the following code if ran*/
        if (map.getTargetElement().style.cursor == "pointer") {
            /*getting the necessary information to pull information from the point in the shapefile*/
            var view = map.getView();
            var viewProjection = view.getProjection();
            var viewResolution = view.getResolution();
            var wms_url = wmsLayer.getSource().getGetFeatureInfoUrl(evt.coordinate, viewResolution, viewProjection, {'INFO_FORMAT': 'text/javascript', }); //Get the wms url for the clicked point
            /*if the point really is the shapfile then the code will get the information and pull out the NAME*/
            if (wms_url) {
                var parser = new ol.format.GeoJSON();
                $.ajax({
                  url: wms_url,
                  dataType: 'jsonp',
                  jsonpCallback: 'parseResponse'
                }).then(function(response) {
                   res_name = response['features'][0]['properties']['NAME']
                   var coord = response['features'][0]['geometry']['coordinates']
                   var coordinate = evt.coordinate;
                   var hdms = ol.coordinate.toStringHDMS(ol.proj.transform(
                        coordinate, 'EPSG:3857', 'EPSG:4326'));

            /*this is what appears in the popup*/
            content.innerHTML = '<h3>' + res_name + '</h3><br><p> Nivel de Agua = ... </p><p> Caudal en entrada = ... </p><p> Ultimo dia de ingresar = ... </p>';
            overlay.setPosition(coordinate);
                });
            map.on("singleclick",function(evt) {

                var res_name_lower;
                if (res_name == "Sabana Yegua")
                   {
                         res_name_lower= 'sabana_yegua';
                   }
                   else if (res_name == "Tavera-Bao")
                   {
                        res_name_lower = 'tavera_bao';
                   }
                   else
                   {
                        res_name_lower = res_name.charAt(0).toLowerCase() + res_name.slice(1);
                   }
                location.href = 'http://127.0.0.1:8000/apps/reservoir-management/' + res_name_lower


            });


            }
        } else {
            /*if the cursor is not a pointer hand, then there is no popup*/
            overlay.setPosition(undefined);
            closer.blur();
            return false;
        }

    });


    /*when the element is clocked, the "goToUrl" function is used, see first function*/
    map.on("singleclick",function(evt) {


        if (map.getTargetElement().style.cursor == "pointer") {


            goToURL()
        }
    });



}

function append(){
    var dam = $("#dam").val();
    var level = $("#levelinput").val();
    var date = $("#dateinput").val();

    $.ajax({
        url: '/apps/reservoir-management/append-res-info/',
        type: 'GET',
        data: {'dam' : dam, 'level' : level, 'date' : date},
        contentType: 'application/json',
        error: function (status) {

        }, success: function (response) {
                location.reload();
        }
    })
}

function test(){
    alert("work")
}

$('#sampleModal').on('show.bs.modal', function () {
    var dam = $("#dam").val();
    var level = $("#levelinput").val();
    var date = $("#dateinput").val();
    levelstr = "Nivel del Embalse = " + level
    datestr = "Dia = " + date;
    document.getElementsByClassName("modal-body")[0].innerHTML = "Embalse = " + dam;
    $( ".modal-body" ).append("<br>");
    $( ".modal-body" ).append("<br>");
    $( ".modal-body" ).append(levelstr);
    $( ".modal-body" ).append("<br>");
    $( ".modal-body" ).append("<br>");
    $( ".modal-body" ).append(datestr);
    warning = '<i class="material-icons" style="font-size:48px;color:red">warning</i>'
    if (level == "") {
        $( ".modal-body" ).append("<br>");
        $( ".modal-body" ).append(warning);
        $( ".modal-body" ).append("<br>");
        $( ".modal-body" ).append('<i style="font-size:25px;color:red">Se necesita un nivel para el embalse</i>')
    }
})

function addvarstomessage(){
    document.getElementsByClassName("modal-body")[0].innerHTML = "Paragraph changed!";
}

function outflowmodal() {
    $("#outflowmod").modal('show')
}

function calculatelevels() {
    var out1 = $("#Outflowday1").val() * $("#Timeday1").val() * 3600
    var out2 = $("#Outflowday2").val() * $("#Timeday2").val() * 3600
    var out3 = $("#Outflowday3").val() * $("#Timeday3").val() * 3600
    var out4 = $("#Outflowday4").val() * $("#Timeday4").val() * 3600
    var out5 = $("#Outflowday5").val() * $("#Timeday5").val() * 3600
    var out6 = $("#Outflowday6").val() * $("#Timeday6").val() * 3600
    var out7 = $("#Outflowday7").val() * $("#Timeday7").val() * 3600
    outflows = [out1,out2,out3,out4,out5,out6,out7].toString()
    console.log(outflows)
    var path = window.location.pathname.split("/");
    var res = path[path.length - 2]
    alert(res);
    var comids = {Chacuey:['1396'],Sabana_Yegua:['593', '600', '599'],Hatillo:['834', '813', '849', '857'],Maguaca:['1399'],Jiguey:['475', '496'],Moncion:['1148', '1182'],Rincon:['853', '922'],Sabaneta:['863', '862'],Tavera:['1024', '1140', '1142', '1153'],Valdesia:['159']};
    comid = comids[res].toString()
    $.ajax({
        url: '/apps/reservoir-management/forecastdata/',
        type: 'GET',
        data: {'comid' : comid, 'res' : res, 'outflows' : outflows},
        contentType: 'application/json',
        error: function (status) {

        }, success: function (response) {
                console.log(response)
        }
    })
}

/*thse function occur automatically when the page is loaded*/
$(function(){
//    $('#app-content-wrapper').removeClass('show-nav');
//    $('#app-actions').remove();
    $(".toggle-nav").removeClass('toggle-nav');
    init_map();
});


