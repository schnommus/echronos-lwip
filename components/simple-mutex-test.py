from prj import Module


class SimpleMutexTestModule(Module):
    xml_schema = """
  <schema>
   <entry name="prefix" type="c_ident" default="rtos_" />
   <entry name="mutexes" type="list" auto_index_field="idx">
     <entry name="mutex" type="dict">
      <entry name="name" type="ident" />
     </entry>
   </entry>
   <entry name="tasks" type="list" auto_index_field="idx">
     <entry name="task" type="dict">
      <entry name="name" type="ident" />
     </entry>
   </entry>
  </schema>
"""
    files = [
        {'input': 'rtos-simple-mutex-test.h', 'render': True},
        {'input': 'rtos-simple-mutex-test.c', 'render': True, 'type': 'c'},
    ]

module = SimpleMutexTestModule()