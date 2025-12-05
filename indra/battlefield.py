import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
from typing import List, Tuple
import random

###
# Import your own quantum library 
###
import quantum_library as qlib

@dataclass
class Soldier:
    """Represents a single soldier on the battlefield."""
    x: int
    y: int
    strength: int
    unit_type: str  # 'soldier', 'knight', 'archer'
    team: str  # 'Quantum' or 'Classical'
    range_dist: int  # combat range
    
    def distance_to(self, other: 'Soldier') -> float:
        """Manhattan distance to another soldier."""
        return abs(self.x - other.x) + abs(self.y - other.y)
        
    def can_fight(self, other: 'Soldier') -> bool:
        """Check if this soldier can fight another."""
        return self.team != other.team and self.distance_to(other) <= self.range_dist
    
class QuantumBattlefield:
    """Manages the battle simulation."""
    def __init__(self, width: int = 4, height: int = 4):
        self.width = width
        self.height = height
        self.board_size = width * height
        self.soldiers: List[Soldier] = []
        self.turn = 0
        self.history = {'team_a_count': [], 'team_b_count': [], 'turn': []}
    
    def add_soldier(self, soldier: Soldier):
        """Add a soldier to the battlefield."""
        self.soldiers.append(soldier)
    
    def initialize_team(self, team: str, composition: dict, start_x_range: Tuple[int, int]):
        """
        Initialize an team with given composition, allowing positions outside the initial width/height.

        Args:
            team: 'Quantum' or 'B'
            composition: {'unit_type': (count, strength, range_dist)}
            start_x_range: (x_min, x_max) for starting positions (inclusive)
        """
        for unit_type, (count, strength, range_dist) in composition.items(): 
            for _ in range(count): 
                x = random.randint(start_x_range[0], start_x_range[1]) 
                y = random.randint(0, self.height-1) 
                soldier = Soldier(x, y, strength, unit_type, team, range_dist) 
                self.add_soldier(soldier)

    def record_history(self):
        """Record current soldier counts for this turn."""
        count_a = sum(1 for s in self.soldiers if s.team == 'Quantum')
        count_b = sum(1 for s in self.soldiers if s.team == 'B')
        self.history['team_a_count'].append(count_a)
        self.history['team_b_count'].append(count_b)
        self.history['turn'].append(self.turn)

    def move_soldiers(self):
        for soldier in self.soldiers:
            if soldier.team == "Quantum":
                # take the best posible move
                # the function must return a tuple best_move = (x,y) based on the current position of the soldier
                # it can accept any desired extra argument
                best_move = qlib.quantum_best_move((soldier.x, soldier.y))
            else:
                # the classical team moves using random walks
                best_move = (random.randint(-1, 1), random.randint(-1, 1))

            # clip to the grid
            new_x = max(0, min(self.width - 1, best_move[0]))
            new_y = max(0, min(self.height - 1, best_move[1]))
            # update position
            soldier.x, soldier.y = new_x, new_y

    def resolve_combat(self):
        """
        Resolve all combats this turn.
        For each pair of adjacent enemies, determine winner and eliminate loser.
        """
        dead_soldiers = set()
        
        for i, soldier1 in enumerate(self.soldiers):
            if i in dead_soldiers:
                continue
            
            for j, soldier2 in enumerate(self.soldiers):
                if i >= j or j in dead_soldiers or i in dead_soldiers:
                    continue
                
                if soldier1.can_fight(soldier2):
                    # Combat!
                    roll1 = soldier1.strength + random.random() * 10
                    roll2 = soldier2.strength + random.random() * 10
                    
                    if roll1 > roll2:
                        dead_soldiers.add(j)
                    else:
                        dead_soldiers.add(i)
        
        # Remove dead soldiers
        self.soldiers = [s for i, s in enumerate(self.soldiers) if i not in dead_soldiers]
    
    def step(self):
        """Execute one turn of the battle."""
        self.move_soldiers()
        self.resolve_combat()
        self.turn += 1
        self.record_history()
    
    def is_battle_over(self) -> bool:
        """Check if battle has ended."""
        count_a = sum(1 for s in self.soldiers if s.team == 'Quantum')
        count_b = sum(1 for s in self.soldiers if s.team == 'Classical')
        return count_a == 0 or count_b == 0
    
    def get_winner(self) -> str:
        """Return 'Quantum', 'Classical', or None."""
        count_a = sum(1 for s in self.soldiers if s.team == 'Quantum')
        count_b = sum(1 for s in self.soldiers if s.team == 'Classical')
        if count_a == 0 and count_b == 0:
            return None
        if count_a == 0:
            return 'Classical'
        if count_b == 0:
            return 'Quantum'
        return None
    
    def get_survivor_count(self) -> Tuple[int, int]:
        """Return (team_a_survivors, team_b_survivors)."""
        count_a = sum(1 for s in self.soldiers if s.team == 'Quantum')
        count_b = sum(1 for s in self.soldiers if s.team == 'Classical')
        return count_a, count_b
    
def visualize_battle(battlefield: QuantumBattlefield, save_path: str = None):
    """Create a static visualization of the battlefield with unit types as markers."""
    fig, ax = plt.subplots()
    
    # Define markers for unit types
    markers = {'soldier': 'o', 'knight': 's', 'archer': '^'}
    colors = {'Quantum': 'royalblue', 'Classical': 'firebrick'}
    
    # Plot each combination of team and unit type
    for team in ['Quantum', 'Classical']:
        for unit_type, marker in markers.items():
            soldiers = [s for s in battlefield.soldiers 
                       if s.team == team and s.unit_type == unit_type]
            if soldiers:
                ax.scatter([s.x for s in soldiers], [s.y for s in soldiers], 
                          c=colors[team], marker=marker, s=100, alpha=0.7,
                          label=f'Team {team} - {unit_type}', edgecolors='black', linewidth=0.5)
    
    ax.set_xlim(-0.1, battlefield.width - 1  + 0.1)
    ax.set_xticks([x for x in range(battlefield.width)])
    ax.set_ylim(-0.1, battlefield.height - 1 + 0.1)
    ax.set_yticks([x for x in range(battlefield.height)])
    ax.set_aspect('equal')
    ax.set_title(f'Battlefield - Turn {battlefield.turn}', fontsize=14, fontweight='bold')
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.legend(loc='upper left', fontsize=9)
    ax.grid(True, alpha=0.3)
    
    if save_path:
        plt.savefig(save_path)
    plt.show()


def plot_history(battlefield: QuantumBattlefield, save_path: str = None):
    """Plot team sizes over time."""
    plt.figure()
    plt.plot(battlefield.history['turn'], battlefield.history['team_a_count'], 
             label='Team Quantum', color='royalblue', linewidth=2)
    plt.plot(battlefield.history['turn'], battlefield.history['team_b_count'], 
             label='Team Firebrick', color='firebrick', linewidth=2)
    plt.xlabel('Turn')
    plt.xticks(battlefield.history['turn'])
    plt.ylabel('Soldier Count')
    plt.title('Team Size Over Time')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    if save_path:
        plt.savefig(save_path)
    plt.show()