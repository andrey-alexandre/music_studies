import string
import random
import time


def tonal_distance(scale: dict, note: str, new_tone: str):
    return (6 + scale[note] - scale[new_tone]) % 6


def create_scale(notes, distances):
    scale = {k: v for k, v in notes if v in distances}
    sorted_scale = dict(sorted(scale.items(), key=lambda item: item[1]))

    return sorted_scale


class Notes:
    def __init__(self):
        self.sequence = {
            "A": 0, "A#": .5, "B": 1, "C": 1.5, "C#": 2, "D": 2.5, "D#": 3, "E": 3.5, "F": 4, "F#": 4.5, "G": 5,
            "G#": 5.5
        }

    def redefine_tone(self, tone):
        self.sequence = {note: tonal_distance(self.sequence, note, tone) for note in self.sequence}


class NaturalScales(Notes):
    def __init__(self, tone, type='Maior'):
        super().__init__()
        self.redefine_tone(tone)

        if type == 'Maior':
            self.distances = [0, 1, 2, 2.5, 3.5, 4.5, 5.5]
        else:
            self.distances = [0, 1, 1.5, 2.5, 3.5, 4, 5]
        self.tone = tone
        self.type = type
        self.scale = create_scale(self.sequence.items(), self.distances)

    def __str__(self):
        return ' '.join(self.scale.keys())

    def __repr__(self):
        return f"Escala {self.type} de {self.tone}"


def input_request():
    input("\t\tPress Enter to continue...")


def check_original_index(original_list, sorted_list, ind):
    return original_list.index(sorted_list[ind])


def train(type, theory='Escala Natural', difficulty='Hard', cycles=100, question_time=60, answer_time=5):
    print("Vamos começar a treinar teoria musical!\n")
    cycle_aux = 0
    degrees = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    while cycle_aux < 7 * cycles:
        inner_cycle = cycle_aux % 7
        if inner_cycle == 0:
            print(f'\tInício do Round {int(1 + cycle_aux/7)}')
            notes_sampled = random.sample(string.ascii_letters[0:7].upper(), k=7)
            degrees_sampled = random.sample(degrees, k=7)

        start_string = f"Grau {degrees_sampled[inner_cycle]} " if difficulty != "Easy" else ""

        print(f'\t\t{start_string}{theory} {type} de {notes_sampled[inner_cycle]}')
        scale = NaturalScales(notes_sampled[inner_cycle], type)

        time.sleep(question_time)
        # input_request()
        if difficulty == 'Easy':
            print(f'\t\t{" - ".join(scale.scale.keys())}')
        else:
            print(f'\t\t{list(scale.scale.keys())[check_original_index(degrees, degrees_sampled, inner_cycle)]}')
        time.sleep(answer_time)
        # input_request()
        cycle_aux += 1

    return None


if __name__ == '__main__':
    a = NaturalScales('D', 'Menor')

    train(type='Maior', question_time=5, answer_time=2)
