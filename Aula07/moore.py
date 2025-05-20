from automata.fa.Moore import Moore

moore = Moore(['q0', 'q1', 'q2', 'q3', 'q4', 'q5'],
              ['0' , '1'],
              ['0', '1'],
              {
                'q0' : {
                    '0' : 'q0',
                    '1' : 'q1'
                    },
                'q1': {
                    '0': 'q0',
                    '1': 'q2'
                    },
                'q2': {
                    '0': 'q3',
                    '1': 'q2'
                    },
                'q3': {
                    '0': 'q0',
                    '1': 'q4'
                    },
                'q4': {
                    '0': 'q0',
                    '1': 'q5'
                    },
                'q5': {
                    '0': 'q3',
                    '1': 'q2'
                    }
                },
                'q0',
                {
                    'q0' : '0',
                    'q1' : '0',
                    'q2' : '0',
                    'q3' : '0',
                    'q4' : '0',
                    'q5' : '1',
                }
                )
print(moore)
input = '11011011'
print('Input:', input)
print('Output:', moore.get_output_from_string(input))