var channel = new goog.appengine.Channel(channelToken);
var socket = channel.open();
var connected = false;
var timeoutId = undefined;
var doc = $('#doc');
var online_count = $('#online_count');
var online_list = $('#online_list');

doc.bind('input propertychange', function() {
  if (timeoutId != undefined) {
    clearTimeout(timeoutId);
  }
  timeoutId = setTimeout(sendPageUpdate, 500);
});

socket.onopen = function() { };

socket.onmessage = function(m) {
  var message = JSON.parse(m.data);
  if (message['text'] != undefined) {
    doc.val(message['text']);
  }
  var ul_inner = '';
  for (var i = 0; i < message['online'].length; i++) {
    if (i >= 10) {
      ul_inner += '<li>...</li>';
      break;
    }
    ul_inner += '<li>' + message['online'][i] + '</li>';
  }
  online_count.html(message['online'].length + '  on the document');
  online_list.html(ul_inner);
};

socket.onerror = function() { };

socket.onclose = function() { };

function sendPageUpdate() {
  sendMessage('update', { 'text': doc.val() });
}

function sendMessage(path, params) {
  var post_params = params || { };
  post_params['doc_id'] = docId;
  $.post(path, post_params, function(data) {  });
}
