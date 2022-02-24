window.Vokabelkarten = {};
window.Vokabelkarten.initialize = function()
{
   $('#hint').hide();
   $('#answer').hide();
}

function show_answer()
{

   $('#answer').show();
   $('#count_this').attr('value', '0')
}