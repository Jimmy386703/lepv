from modules.utils.socketIOBlueprint import SocketIOBlueprint
from flask_socketio import emit
from modules.profilers.memory.MemoryProfiler import MemoryProfiler

memory_blueprint = SocketIOBlueprint('')


@memory_blueprint.on('memory.status.req')
def get_memory_status(request):
    print('received memory.status.req: ' + request['server'])

    server = request['server']
    profiler = MemoryProfiler(server)
    data = {}
    data = profiler.getStatus()

    if "request_id" in request:
        data['response_id'] = request['request_id']

    emit('memory.status.res', data)


@memory_blueprint.on('memory.procrank.req')
def get_proc_rank(request):
    print('received memory.procrank.req: ' + request['server'])

    server = request['server']
    profiler = MemoryProfiler(server)
    data = profiler.getProcrank()

    if "request_id" in request:
        data['response_id'] = request['request_id']

    emit('memory.procrank.res',  data)