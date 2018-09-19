
$( document ).ready(function() {
    console.log( "ready!" );



function HFViewModel() {
    var self = this;
    self.hflipper = ko.observableArray([]);

    flipIt=function(){
        console.log('Flip Started')
        $.get('/flip',function(data){

            self.hflipper(JSON.parse(data))
            console.log(self.hflipper())
        });
    }
    flipIt();
};


ko.applyBindings(new HFViewModel());
});