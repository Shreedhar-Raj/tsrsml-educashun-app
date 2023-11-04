import jsonlines
import json

training_data = [
    {
    "prompt": "Physics, Unit 1: Motion, Forces and Energy, easy, What is Newton's first law of motion?",
    "completion": "Option 1: An object will remain at rest or in uniform motion unless acted upon by a force, Option 2: F = ma, Option 3: For every action, there is an equal and opposite reaction, Option 4: Energy cannot be created nor destroyed, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 1: Motion, Forces and Energy, easy, What is Newton's first law of motion?",
    "completion": "Option 1: An object will remain at rest or in uniform motion unless acted upon by a force, Option 2: F = ma, Option 3: For every action, there is an equal and opposite reaction, Option 4: Energy cannot be created nor destroyed, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 1: Motion, Forces and Energy, easy, What is the unit of force?",
    "completion": "Option 1: Newton, Option 2: Joule, Option 3: Watt, Option 4: Meter, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 1: Motion, Forces and Energy, medium, What is the work done on an object when a force of 5 N is applied over a distance of 3 m?",
    "completion": "Option 1: 15 Joules, Option 2: 8 Joules, Option 3: 10 Joules, Option 4: 20 Joules, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 1: Motion, Forces and Energy, medium, What is the potential energy of a 5 kg object held 10 m above the ground?",
    "completion": "Option 1: 500 Joules, Option 2: 50 Joules, Option 3: 100 Joules, Option 4: 250 Joules, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 1: Motion, Forces and Energy, hard, What is the principle of conservation of mechanical energy?",
    "completion": "Option 1: The total mechanical energy remains constant in an isolated system, Option 2: Energy can neither be created nor destroyed, Option 3: The total mechanical energy decreases in an isolated system, Option 4: Energy can be transformed from one form to another, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 1: Motion, Forces and Energy, hard, What is the equation for kinetic energy?",
    "completion": "Option 1: KE = 1/2 mv^2, Option 2: KE = mv, Option 3: KE = mgh, Option 4: KE = Fd, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 2: Thermal Physics, easy, What is the unit of temperature in the International System of Units?",
    "completion": "Option 1: Kelvin, Option 2: Celsius, Option 3: Fahrenheit, Option 4: Rankine, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 2: Thermal Physics, easy, What is thermal equilibrium?",
    "completion": "Option 1: When two systems are at the same temperature, Option 2: When heat flows from a hot body to a cold body, Option 3: When a body's temperature remains constant, Option 4: When a body's temperature is increasing, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 2: Thermal Physics, medium, What is the formula for calculating heat transferred?",
    "completion": "Option 1: Q = mcΔT, Option 2: Q = mv, Option 3: Q = ma, Option 4: Q = mc^2, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 2: Thermal Physics, medium, What is the specific heat capacity?",
    "completion": "Option 1: The amount of heat required to raise the temperature of a unit mass of a substance by one degree Celsius, Option 2: The amount of heat that flows per unit time, Option 3: The total amount of heat in a system, Option 4: The heat capacity per mole of a substance, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 2: Thermal Physics, hard, What is the principle of heat engines?",
    "completion": "Option 1: Converting heat into work, Option 2: Converting work into heat, Option 3: Maintaining a constant temperature, Option 4: Preventing heat transfer, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 2: Thermal Physics, hard, What is entropy?",
    "completion": "Option 1: A measure of the disorder of a system, Option 2: A measure of the energy of a system, Option 3: A measure of the temperature of a system, Option 4: A measure of the pressure of a system, Correct Option: Option 1"
    },
    {
     "prompt": "Physics, Unit 3: Waves, easy, What is the frequency of a wave?",
    "completion": "Option 1: The number of wave cycles per unit time, Option 2: The distance between two wave crests, Option 3: The height of a wave crest, Option 4: The speed of a wave, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 3: Waves, easy, What is the amplitude of a wave?",
    "completion": "Option 1: The maximum displacement of a wave from its rest position, Option 2: The distance between two wave crests, Option 3: The speed of a wave, Option 4: The number of wave cycles per unit time, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 3: Waves, medium, What is the principle of superposition?",
    "completion": "Option 1: The displacement of a point due to the superposition of wave systems is equal to the sum of the displacements of individual waves at that point, Option 2: Waves can cancel each other out, Option 3: Waves can reinforce each other, Option 4: Waves can reflect off boundaries, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 3: Waves, medium, What is the formula for the speed of a wave?",
    "completion": "Option 1: v = fλ, Option 2: v = f^2, Option 3: v = λ^2, Option 4: v = ft, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 3: Waves, hard, What is the Doppler effect?",
    "completion": "Option 1: A change in frequency or wavelength of a wave in relation to an observer, Option 2: The reflection of waves off a boundary, Option 3: The refraction of waves through a medium, Option 4: The interference of waves, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 3: Waves, hard, What is the difference between transverse and longitudinal waves?",
    "completion": "Option 1: Transverse waves oscillate perpendicular to the direction of the wave, while longitudinal waves oscillate parallel to the direction of the wave, Option 2: Transverse waves oscillate parallel to the direction of the wave, while longitudinal waves oscillate perpendicular to the direction of the wave, Option 3: Transverse waves have a higher frequency, Option 4: Longitudinal waves have a higher frequency, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 4: Electricity and Magnetism, easy, What is the unit of electric charge?",
    "completion": "Option 1: Coulomb, Option 2: Ampere, Option 3: Volt, Option 4: Ohm, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 4: Electricity and Magnetism, easy, What is Ohm's Law?",
    "completion": "Option 1: V = IR, Option 2: V = I/R, Option 3: V = I^2R, Option 4: V = IR^2, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 4: Electricity and Magnetism, medium, What is the principle of electromagnetic induction?",
    "completion": "Option 1: The production of an electromotive force across a conductor when it is exposed to a varying magnetic field, Option 2: The production of a magnetic field by an electric current, Option 3: The attraction or repulsion between electric charges, Option 4: The attraction or repulsion between magnetic poles, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 4: Electricity and Magnetism, medium, What is the formula for calculating the magnetic field strength of a long straight current-carrying wire?",
    "completion": "Option 1: B = μ₀I/(2πr), Option 2: B = μ₀I/(πr^2), Option 3: B = μ₀I/(4πr), Option 4: B = μ₀I/(πr), Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 4: Electricity and Magnetism, hard, What is the Lorentz force?",
    "completion": "Option 1: The force experienced by a charged particle moving through an electric and magnetic field, Option 2: The force between two electric charges, Option 3: The force between two magnetic poles, Option 4: The force of gravity on a charged particle, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 4: Electricity and Magnetism, hard, What is the principle of the motor effect?",
    "completion": "Option 1: A current-carrying wire in a magnetic field experiences a force, Option 2: A wire moving in a magnetic field produces an electric current, Option 3: A changing magnetic field produces an electric current, Option 4: A steady magnetic field produces an electric current, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 5: Nuclear Physics, easy, What is the strong nuclear force?",
    "completion": "Option 1: The force that holds protons and neutrons together in the nucleus, Option 2: The force between electrons and protons, Option 3: The force of gravity on a nucleus, Option 4: The force that holds electrons in their orbits, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 5: Nuclear Physics, easy, What is radioactive decay?",
    "completion": "Option 1: The process by which an unstable atomic nucleus loses energy by radiation, Option 2: The process by which a nucleus gains energy by absorbing radiation, Option 3: The process by which a nucleus fuses with another nucleus, Option 4: The process by which a nucleus splits into two smaller nuclei, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 5: Nuclear Physics, medium, What is the difference between nuclear fission and nuclear fusion?",
    "completion": "Option 1: Nuclear fission is the splitting of a large atomic nucleus into smaller particles, while nuclear fusion is the coming together of two light atomic nuclei to form a heavier nucleus, Option 2: Nuclear fission is the coming together of two light atomic nuclei to form a heavier nucleus, while nuclear fusion is the splitting of a large atomic nucleus into smaller particles, Option 3: Nuclear fission releases more energy than nuclear fusion, Option 4: Nuclear fusion releases more energy than nuclear fission, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 5: Nuclear Physics, medium, What is the principle behind nuclear reactors?",
    "completion": "Option 1: Nuclear fission reactions provide the energy to heat water, creating steam to drive turbines and generate electricity, Option 2: Nuclear fusion reactions provide the energy to heat water, creating steam to drive turbines and generate electricity, Option 3: Chemical reactions provide the energy to heat water, creating steam to drive turbines and generate electricity, Option 4: Solar energy provides the energy to heat water, creating steam to drive turbines and generate electricity, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 5: Nuclear Physics, hard, What is mass defect?",
    "completion": "Option 1: The difference between the mass of a nucleus and the sum of the masses of its individual protons and neutrons, Option 2: The mass of a nucleus, Option 3: The mass of an atom, Option 4: The difference between the mass of an atom and the sum of the masses of its individual electrons, protons, and neutrons, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 5: Nuclear Physics, hard, What is the principle of conservation of charge?",
    "completion": "Option 1: The total charge in an isolated system remains constant, Option 2: Charge can be created or destroyed, Option 3: The charge of a system is always positive, Option 4: The charge of a system is always negative, Correct Option: Option 1"
    },
    {"prompt": "Physics, Unit 6: Space Physics, easy, What is a black hole?",
    "completion": "Option 1: A region of space where the gravitational field is so strong that nothing, not even light, can escape from it, Option 2: A region of space where light is emitted, Option 3: A region of space where stars add more entries"},
    {
    "prompt": "Physics, Unit 6: Space Physics, medium, What is the formula for the escape velocity from the surface of a planet?",
    "completion": "Option 1: ve = sqrt(2GM/R), Option 2: ve = GM/R, Option 3: ve = sqrt(GM/R), Option 4: ve = 2GM/R, Correct Option: Option 1"},
    {
    "prompt": "Physics, Unit 6: Space Physics, medium, What is the formula for the escape velocity from the surface of a planet?",
    "completion": "Option 1: ve = sqrt(2GM/R), Option 2: ve = GM/R, Option 3: ve = sqrt(GM/R), Option 4: ve = 2GM/R, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 6: Space Physics, hard, What is the concept of spacetime curvature in General Relativity?",
    "completion": "Option 1: Massive objects curve the spacetime around them, Option 2: Time flows backwards in curved spacetime, Option 3: Spacetime is flat in the presence of mass, Option 4: Curved spacetime is an illusion, Correct Option: Option 1"
    },
    {
    "prompt": "Physics, Unit 6: Space Physics, hard, What is the Schwarzschild radius?",
    "completion": "Option 1: The radius below which a mass becomes a black hole, Option 2: The radius of the event horizon, Option 3: The radius of the accretion disk around a black hole, Option 4: The maximum radius of a stable orbit around a black hole, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 1: The particulate nature of matter, easy, What is the basic building block of matter?",
    "completion": "Option 1: Atom, Option 2: Molecule, Option 3: Electron, Option 4: Compound, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 1: The particulate nature of matter, easy, Which state of matter has a definite shape and volume?",
    "completion": "Option 1: Solid, Option 2: Liquid, Option 3: Gas, Option 4: Plasma, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 1: The particulate nature of matter, medium, What is the process of a solid turning into a liquid called?",
    "completion": "Option 1: Melting, Option 2: Freezing, Option 3: Vaporization, Option 4: Condensation, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 1: The particulate nature of matter, medium, Which of the following is a characteristic of a gas?",
    "completion": "Option 1: Definite volume, Option 2: Indefinite shape, Option 3: Definite shape, Option 4: Indefinite volume, Correct Option: Option 2"
    },
    {
    "prompt": "Chemistry, Unit 1: The particulate nature of matter, hard, Which principle states that matter can neither be created nor destroyed?",
    "completion": "Option 1: Law of Conservation of Mass, Option 2: Law of Definite Proportions, Option 3: Law of Multiple Proportions, Option 4: Avogadro's Hypothesis, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 1: The particulate nature of matter, hard, What is the name of the region where electrons are likely to be found in an atom?",
    "completion": "Option 1: Nucleus, Option 2: Electron cloud, Option 3: Orbital, Option 4: Shell, Correct Option: Option 3"
    },
    {
    "prompt": "Chemistry, Unit 2: Experimental Techniques, easy, What is the process of separating a solid from a liquid called?",
    "completion": "Option 1: Filtration, Option 2: Distillation, Option 3: Chromatography, Option 4: Sublimation, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 2: Experimental Techniques, easy, Which technique is used to separate mixtures based on their boiling points?",
    "completion": "Option 1: Distillation, Option 2: Filtration, Option 3: Chromatography, Option 4: Crystallization, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 2: Experimental Techniques, medium, In which process is a solute separated from a solution by crystallizing out?",
    "completion": "Option 1: Crystallization, Option 2: Distillation, Option 3: Filtration, Option 4: Chromatography, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 2: Experimental Techniques, medium, Which of the following is a method to determine the concentration of a solution?",
    "completion": "Option 1: Titration, Option 2: Filtration, Option 3: Distillation, Option 4: Sublimation, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 2: Experimental Techniques, hard, What is the process of separating substances based on their molecular sizes and shapes called?",
    "completion": "Option 1: Chromatography, Option 2: Filtration, Option 3: Distillation, Option 4: Titration, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 2: Experimental Techniques, hard, What is the process of measuring the volume of gas evolved in a reaction called?",
    "completion": "Option 1: Gas collection, Option 2: Titration, Option 3: Filtration, Option 4: Distillation, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 3: Atoms, elements and compounds, easy, What is the smallest unit of an element that retains the properties of that element?",
    "completion": "Option 1: Atom, Option 2: Molecule, Option 3: Compound, Option 4: Ion, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 3: Atoms, elements and compounds, easy, What is a substance made up of two or more different types of atoms chemically bonded together?",
    "completion": "Option 1: Compound, Option 2: Mixture, Option 3: Element, Option 4: Solution, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 3: Atoms, elements and compounds, medium, What is the charge of a proton?",
    "completion": "Option 1: +1, Option 2: -1, Option 3: 0, Option 4: +2, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 3: Atoms, elements and compounds, medium, Which subatomic particle has no charge?",
    "completion": "Option 1: Neutron, Option 2: Proton, Option 3: Electron, Option 4: Ion, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 3: Atoms, elements and compounds, hard, What is the name of the vertical columns in the periodic table?",
    "completion": "Option 1: Groups, Option 2: Periods, Option 3: Blocks, Option 4: Families, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 3: Atoms, elements and compounds, hard, What is the atomic number of an element?",
    "completion": "Option 1: The number of protons in the nucleus, Option 2: The number of neutrons in the nucleus, Option 3: The number of electrons in the shell, Option 4: The total number of protons and neutrons in the nucleus, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 4: Stoichiometry, easy, What is the molar mass of water?",
    "completion": "Option 1: 18 g/mol, Option 2: 16 g/mol, Option 3: 20 g/mol, Option 4: 22 g/mol, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 4: Stoichiometry, easy, What is the balanced equation for the combustion of methane?",
    "completion": "Option 1: CH4 + 2O2 -> CO2 + 2H2O, Option 2: CH4 + O2 -> CO2 + H2O, Option 3: CH4 + 3O2 -> CO2 + 2H2O, Option 4: CH4 + O2 -> CO + H2O, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 4: Stoichiometry, medium, How many moles of oxygen are required to react with 2 moles of hydrogen to form water?",
    "completion": "Option 1: 1 mole, Option 2: 2 moles, Option 3: 3 moles, Option 4: 4 moles, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 4: Stoichiometry, medium, What is the percentage composition of oxygen in water?",
    "completion": "Option 1: 88.8%, Option 2: 11.2%, Option 3: 50%, Option 4: 25%, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 4: Stoichiometry, hard, What is the law of conservation of mass?",
    "completion": "Option 1: Mass cannot be created or destroyed in a chemical reaction, Option 2: Mass is always conserved in a chemical reaction, Option 3: Mass can be created or destroyed in a chemical reaction, Option 4: Mass is always created in a chemical reaction, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 4: Stoichiometry, hard, What is the name of the law that states that a given compound always contains exactly the same proportion of elements by mass?",
    "completion": "Option 1: Law of Definite Proportions, Option 2: Law of Conservation of Mass, Option 3: Law of Multiple Proportions, Option 4: Avogadro's Law, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 5: Electricity and Chemistry, easy, What is the process of using electricity to drive a non-spontaneous reaction called?",
    "completion": "Option 1: Electrolysis, Option 2: Electroplating, Option 3: Electrorefining, Option 4: Galvanization, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 5: Electricity and Chemistry, easy, What is the device used to measure electric current called?",
    "completion": "Option 1: Ammeter, Option 2: Voltmeter, Option 3: Ohmmeter, Option 4: Galvanometer, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 5: Electricity and Chemistry, medium, What is the term for the loss of electrons in a chemical reaction?",
    "completion": "Option 1: Oxidation, Option 2: Reduction, Option 3: Electrolysis, Option 4: Electroplating, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 5: Electricity and Chemistry, medium, What is a half-cell in electrochemistry?",
    "completion": "Option 1: A structure that contains a conductive electrode and a surrounding conductive electrolyte separated by a naturally occurring Helmholtz double layer, Option 2: A full cell divided in half, Option 3: A cell with half the voltage of a full cell, Option 4: A cell with half the electrolyte of a full cell, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 5: Electricity and Chemistry, hard, What is the standard electrode potential?",
    "completion": "Option 1: The measure of the potential of a reversible cell when all reactants and products are at their standard states, Option 2: The measure of the potential of an irreversible cell when all reactants and products are at their standard states, Option 3: The measure of the potential of a reversible cell when all reactants and products are at non-standard states, Option 4: The measure of the potential of an irreversible cell when all reactants and products are at non-standard states, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 5: Electricity and Chemistry, hard, What is Faraday's Law of Electrolysis?",
    "completion": "Option 1: The amount of substance produced at an electrode during electrolysis is directly proportional to the number of moles of electrons transferred at that electrode, Option 2: The amount of substance produced at an electrode during electrolysis is inversely proportional to the number of moles of electrons transferred at that electrode, Option 3: The amount of substance produced at an electrode during electrolysis is directly proportional to the voltage applied across the cell, Option 4: The amount of substance produced at an electrode during electrolysis is inversely proportional to the voltage applied across the cell, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 6: Chemical energetics, easy, What is the term for the amount of energy needed to raise the temperature of 1 gram of water by 1 degree Celsius?",
    "completion": "Option 1: Calorie, Option 2: Joule, Option 3: Watt, Option 4: Kelvin, Correct Option: Option 1"
    },
    {
        "prompt": "Chemistry, Unit 6: Chemical energetics, easy, What is the law of conservation of energy?",
        "completion": "Option 1: Energy cannot be created or destroyed, only transferred or converted from one form to another, Option 2: Energy can be created and destroyed, Option 3: Energy is always lost as heat in a reaction, Option 4: Energy is always conserved in a reaction, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 6: Chemical energetics, medium, What is the term for the amount of energy released or absorbed during a chemical reaction?",
    "completion": "Option 1: Enthalpy change, Option 2: Entropy change, Option 3: Heat capacity, Option 4: Activation energy, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 6: Chemical energetics, medium, What is the energy required to initiate a reaction called?",
    "completion": "Option 1: Activation energy, Option 2: Reaction energy, Option 3: Enthalpy, Option 4: Gibbs free energy, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 6: Chemical energetics, hard, What is the formula for calculating the change in Gibbs free energy?",
    "completion": "Option 1: ΔG = ΔH - TΔS, Option 2: ΔG = ΔH + TΔS, Option 3: ΔG = TΔS - ΔH, Option 4: ΔG = TΔS + ΔH, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 6: Chemical energetics, hard, What is the term for a reaction where energy is released?",
    "completion": "Option 1: Exothermic, Option 2: Endothermic, Option 3: Isotonic, Option 4: Hypertonic, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 7: Reaction kinetics, easy, What is the term for the speed at which a reaction occurs?",
    "completion": "Option 1: Reaction rate, Option 2: Reaction time, Option 3: Reaction speed, Option 4: Reaction path, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 7: Reaction kinetics, easy, What is the term for a substance that speeds up a reaction without being consumed?",
    "completion": "Option 1: Catalyst, Option 2: Reactant, Option 3: Product, Option 4: Inhibitor, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 7: Reaction kinetics, medium, What is the term for the highest point on the reaction coordinate diagram?",
    "completion": "Option 1: Transition state, Option 2: Activation energy, Option 3: Reaction intermediate, Option 4: Reaction endpoint, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 7: Reaction kinetics, medium, What is the term for a substance that slows down a reaction?",
    "completion": "Option 1: Inhibitor, Option 2: Catalyst, Option 3: Reactant, Option 4: Product, Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 7: Reaction kinetics, hard, What is the formula for the rate law of a reaction?",
    "completion": "Option 1: Rate = k[A]^m[B]^n, Option 2: Rate = k[A][B], Option 3: Rate = k[A] + k[B], Option 4: Rate = k[A] - k[B], Correct Option: Option 1"
    },
    {
    "prompt": "Chemistry, Unit 7: Reaction kinetics, hard, What is the effect of increasing the temperature on the rate of a reaction?",
    "completion": "Option 1: Increases the rate of reaction, Option 2: Decreases the rate of reaction, Option 3: No effect on the rate of reaction, Option 4: Changes the products of the reaction, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 1: Characteristics and classification of living organisms, easy, What is the basic unit of life?",
        "completion": "Option 1: Cell, Option 2: Atom, Option 3: Molecule, Option 4: Organ, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 1: Characteristics and classification of living organisms, easy, What are the three domains of life?",
        "completion": "Option 1: Bacteria, Archaea, Eukarya, Option 2: Animals, Plants, Fungi, Option 3: Monera, Protista, Fungi, Option 4: Prokaryotes, Eukaryotes, Viruses, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 1: Characteristics and classification of living organisms, medium, What is the difference between prokaryotic and eukaryotic cells?",
        "completion": "Option 1: Prokaryotic cells lack a nucleus and membrane-bound organelles, while eukaryotic cells have a nucleus and membrane-bound organelles, Option 2: Prokaryotic cells have a nucleus, while eukaryotic cells do not, Option 3: Prokaryotic cells are larger than eukaryotic cells, Option 4: Eukaryotic cells reproduce by binary fission, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 1: Characteristics and classification of living organisms, medium, What is the hierarchy of biological classification from domain to species?",
        "completion": "Option 1: Domain, Kingdom, Phylum, Class, Order, Family, Genus, Species, Option 2: Kingdom, Domain, Phylum, Class, Order, Family, Genus, Species, Option 3: Domain, Phylum, Kingdom, Class, Order, Family, Genus, Species, Option 4: Kingdom, Phylum, Class, Order, Family, Genus, Species, Domain, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 1: Characteristics and classification of living organisms, hard, What is binomial nomenclature and who introduced it?",
        "completion": "Option 1: A system of naming species using two names, genus and species, introduced by Carl Linnaeus, Option 2: A system of naming species using two names, family and species, introduced by Charles Darwin, Option 3: A system of naming species using one name, introduced by Carl Linnaeus, Option 4: A system of naming species using three names, introduced by Charles Darwin, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 1: Characteristics and classification of living organisms, hard, What are the five kingdoms of life?",
        "completion": "Option 1: Monera, Protista, Fungi, Plantae, Animalia, Option 2: Bacteria, Archaea, Protista, Plantae, Animalia, Option 3: Monera, Protista, Plantae, Animalia, Fungi, Option 4: Protista, Fungi, Plantae, Animalia, Viruses, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 2: Organization of the organism, easy, What is the term for a group of cells with a similar structure and function?",
        "completion": "Option 1: Tissue, Option 2: Organ, Option 3: System, Option 4: Organism, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 2: Organization of the organism, easy, What is the term for a group of tissues working together to perform a specific function?",
        "completion": "Option 1: Organ, Option 2: System, Option 3: Organism, Option 4: Cell, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 2: Organization of the organism, medium, What are the three types of muscle tissue?",
        "completion": "Option 1: Skeletal, Cardiac, Smooth, Option 2: Bone, Cardiac, Smooth, Option 3: Skeletal, Cardiac, Nervous, Option 4: Skeletal, Smooth, Epithelial, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 2: Organization of the organism, medium, What is the function of the nervous tissue?",
        "completion": "Option 1: Transmitting electrical signals for communication, Option 2: Providing support and structure, Option 3: Contracting to produce movement, Option 4: Covering body surfaces and lining body cavities, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 2: Organization of the organism, hard, What is homeostasis and why is it important?",
        "completion": "Option 1: The maintenance of a stable internal environment, crucial for the survival and functioning of the organism, Option 2: The ability to adapt to changes in the external environment, Option 3: The ability to reproduce and pass on genetic information, Option 4: The ability to respond to stimuli, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 2: Organization of the organism, hard, What is the function of the lymphatic system?",
        "completion": "Option 1: Draining excess fluid from tissues, transporting white blood cells, and aiding in immunity, Option 2: Circulating blood and delivering nutrients, Option 3: Digesting food and absorbing nutrients, Option 4: Excreting waste products, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 3: Movement in and out of cells, easy, What is osmosis?",
        "completion": "Option 1: The movement of water molecules from an area of lower solute concentration to an area of higher solute concentration through a selectively permeable membrane, Option 2: The movement of solute molecules from an area of higher concentration to an area of lower concentration, Option 3: The movement of water molecules from an area of higher concentration to an area of lower concentration, Option 4: The movement of solute molecules from an area of lower concentration to an area of higher concentration, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 3: Movement in and out of cells, easy, What is diffusion?",
        "completion": "Option 1: The movement of molecules from an area of higher concentration to an area of lower concentration, Option 2: The movement of water molecules across a selectively permeable membrane, Option 3: The movement of molecules from an area of lower concentration to an area of higher concentration, Option 4: The movement of molecules against a concentration gradient, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 3: Movement in and out of cells, medium, What is active transport?",
        "completion": "Option 1: The movement of molecules against a concentration gradient, requiring energy, Option 2: The movement of molecules down a concentration gradient, Option 3: The movement of water molecules across a membrane, Option 4: The movement of molecules without the use of energy, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 3: Movement in and out of cells, medium, What is the term for the uptake of large particles or cells by surrounding and engulfing them?",
        "completion": "Option 1: Phagocytosis, Option 2: Pinocytosis, Option 3: Exocytosis, Option 4: Endocytosis, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 3: Movement in and out of cells, hard, What is the sodium-potassium pump and why is it important?",
        "completion": "Option 1: A protein that actively transports sodium ions out and potassium ions into the cell, crucial for maintaining membrane potential and cell function, Option 2: A protein that passively transports sodium and potassium ions, Option 3: A pump that moves water in and out of the cell, Option 4: A protein that actively transports potassium ions out and sodium ions into the cell, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 3: Movement in and out of cells, hard, What is the difference between endocytosis and exocytosis?",
        "completion": "Option 1: Endocytosis is the uptake of material into the cell by invagination of the cell membrane, while exocytosis is the release of material from the cell by fusion of a vesicle with the cell membrane, Option 2: Endocytosis is the release of material from the cell, while exocytosis is the uptake of material into the cell, Option 3: Endocytosis requires energy, while exocytosis does not, Option 4: Endocytosis and exocytosis are the same process, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 4: Biological molecules, easy, What is the basic unit of a carbohydrate?",
        "completion": "Option 1: Monosaccharide, Option 2: Amino acid, Option 3: Nucleotide, Option 4: Fatty acid, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 4: Biological molecules, easy, What is the main function of lipids in the body?",
        "completion": "Option 1: Energy storage, Option 2: Speeding up chemical reactions, Option 3: Transmitting genetic information, Option 4: Providing structural support, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 4: Biological molecules, medium, What is the term for a molecule that speeds up a chemical reaction without being consumed?",
        "completion": "Option 1: Catalyst, Option 2: Reactant, Option 3: Product, Option 4: Enzyme, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 4: Biological molecules, medium, What is the function of nucleic acids?",
        "completion": "Option 1: Storing and transmitting genetic information, Option 2: Providing energy, Option 3: Speeding up chemical reactions, Option 4: Providing structural support, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 4: Biological molecules, hard, What is the primary structure of a protein?",
        "completion": "Option 1: The sequence of amino acids in a polypeptide chain, Option 2: The folding of a polypeptide chain into a 3D shape, Option 3: The arrangement of multiple polypeptide chains, Option 4: The addition of functional groups to a polypeptide chain, Correct Option: Option 1"
    },
        {
        "prompt": "Biology, Unit 4: Biological molecules, hard, What is the difference between DNA and RNA?",
        "completion": "Option 1: DNA is double-stranded and contains deoxyribose sugar, while RNA is single-stranded and contains ribose sugar, Option 2: DNA is single-stranded and contains ribose sugar, while RNA is double-stranded and contains deoxyribose sugar, Option 3: DNA contains uracil, while RNA contains thymine, Option 4: DNA is found in the cytoplasm, while RNA is found in the nucleus, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 5: Enzymes, easy, What is an enzyme?",
        "completion": "Option 1: A biological catalyst that speeds up chemical reactions in living organisms, Option 2: A type of carbohydrate, Option 3: A type of lipid, Option 4: A type of nucleic acid, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 5: Enzymes, easy, What part of the enzyme binds to the substrate?",
        "completion": "Option 1: Active site, Option 2: Allosteric site, Option 3: Binding site, Option 4: Catalytic site, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 5: Enzymes, medium, What factors can affect enzyme activity?",
        "completion": "Option 1: Temperature, pH, and substrate concentration, Option 2: Color, shape, and size, Option 3: Mass, volume, and density, Option 4: Speed, velocity, and acceleration, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 5: Enzymes, medium, What is enzyme inhibition?",
        "completion": "Option 1: A process where a molecule binds to an enzyme and decreases its activity, Option 2: A process where a molecule binds to an enzyme and increases its activity, Option 3: A process where an enzyme breaks down a molecule, Option 4: A process where an enzyme builds up a molecule, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 5: Enzymes, hard, What is the difference between competitive and non-competitive inhibition?",
        "completion": "Option 1: Competitive inhibition occurs when a molecule similar to the substrate binds to the active site, while non-competitive inhibition occurs when a molecule binds to an allosteric site, changing the enzyme's shape, Option 2: Competitive inhibition occurs when a molecule binds to an allosteric site, while non-competitive inhibition occurs when a molecule similar to the substrate binds to the active site, Option 3: Competitive inhibition increases enzyme activity, while non-competitive inhibition decreases enzyme activity, Option 4: Competitive inhibition decreases enzyme activity, while non-competitive inhibition increases enzyme activity, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 6: Plant nutrition, easy, What is photosynthesis?",
        "completion": "Option 1: The process by which green plants and some other organisms use sunlight to synthesize foods with the help of chlorophyll pigments, Option 2: The process by which plants break down food to produce energy, Option 3: The process by which plants consume nutrients from the soil, Option 4: The process by which plants absorb water, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 6: Plant nutrition, easy, What are the main raw materials for photosynthesis?",
        "completion": "Option 1: Carbon dioxide and water, Option 2: Oxygen and glucose, Option 3: Nitrogen and phosphorus, Option 4: Vitamins and minerals, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 6: Plant nutrition, medium, What is the main pigment involved in photosynthesis?",
        "completion": "Option 1: Chlorophyll, Option 2: Carotene, Option 3: Xanthophyll, Option 4: Anthocyanin, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 6: Plant nutrition, medium, What are micronutrients and why are they important for plants?",
        "completion": "Option 1: Micronutrients are essential elements required by plants in small amounts for growth and development, Option 2: Micronutrients are the main nutrients required by plants, Option 3: Micronutrients are organic compounds required by plants, Option 4: Micronutrients are nutrients required by animals but not plants, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 6: Plant nutrition, hard, What is the difference between the light-dependent and light-independent reactions in photosynthesis?",
        "completion": "Option 1: Light-dependent reactions occur in the thylakoid membranes and produce ATP and NADPH, while light-independent reactions occur in the stroma and use ATP and NADPH to fix carbon dioxide and produce glucose, Option 2: Light-dependent reactions occur in the stroma and produce glucose, while light-independent reactions occur in the thylakoid membranes and produce ATP and NADPH, Option 3: Light-dependent reactions use carbon dioxide to produce glucose, while light-independent reactions use sunlight to produce ATP and NADPH, Option 4: Light-dependent reactions use ATP and NADPH to fix carbon dioxide and produce glucose, while light-independent reactions produce ATP and NADPH, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 7: Human nutrition, easy, What is the main function of carbohydrates in the human diet?",
        "completion": "Option 1: Providing energy, Option 2: Building and repairing tissues, Option 3: Regulating body processes, Option 4: Providing insulation, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 7: Human nutrition, easy, What is the function of dietary fiber?",
        "completion": "Option 1: Aiding in digestion and preventing constipation, Option 2: Providing energy, Option 3: Building and repairing tissues, Option 4: Regulating body processes, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 7: Human nutrition, medium, What are the essential amino acids and why are they important?",
        "completion": "Option 1: Amino acids that cannot be synthesized by the body and must be obtained from the diet, essential for protein synthesis and overall growth and development, Option 2: Amino acids that can be synthesized by the body, Option 3: Amino acids that provide energy, Option 4: Amino acids that help in digestion, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 7: Human nutrition, medium, What is the function of vitamins and minerals in the human diet?",
        "completion": "Option 1: Supporting overall growth and development, immune function, and metabolism, Option 2: Providing energy, Option 3: Building and repairing tissues, Option 4: Aiding in digestion, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 7: Human nutrition, hard, What is the difference between saturated and unsaturated fats?",
        "completion": "Option 1: Saturated fats have no double bonds between the fatty acid molecules, while unsaturated fats have one or more double bonds, Option 2: Saturated fats have one or more double bonds, while unsaturated fats have no double bonds, Option 3: Saturated fats are liquid at room temperature, while unsaturated fats are solid, Option 4: Saturated fats are healthy, while unsaturated fats are unhealthy, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 8: Transport in plants, easy, What is transpiration?",
        "completion": "Option 1: The process of water movement through a plant and its evaporation from aerial parts, especially from the leaves but also from stems and flowers, Option 2: The process of water absorption by the roots, Option 3: The process of water transportation through the xylem, Option 4: The process of nutrient absorption by the leaves, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 8: Transport in plants, easy, What are the two main types of vascular tissue in plants?",
        "completion": "Option 1: Xylem and Phloem, Option 2: Epidermis and Cortex, Option 3: Mesophyll and Epidermis, Option 4: Periderm and Mesophyll, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 8: Transport in plants, medium, What is the function of the xylem?",
        "completion": "Option 1: Transporting water and minerals from the roots to the rest of the plant, Option 2: Transporting sugars and other nutrients from the leaves to the rest of the plant, Option 3: Providing structural support to the plant, Option 4: Aiding in photosynthesis, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 8: Transport in plants, medium, What is the function of the phloem?",
        "completion": "Option 1: Transporting sugars and other nutrients from the leaves to the rest of the plant, Option 2: Transporting water and minerals from the roots to the rest of the plant, Option 3: Providing structural support to the plant, Option 4: Aiding in photosynthesis, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 8: Transport in plants, hard, What is the difference between apoplastic and symplastic pathways of water movement in plants?",
        "completion": "Option 1: Apoplastic pathway involves the movement of water through the cell walls and spaces between cells, while symplastic pathway involves the movement of water through the cytoplasm of cells, Option 2: Apoplastic pathway involves the movement of water through the cytoplasm of cells, while symplastic pathway involves the movement of water through the cell walls and spaces between cells, Option 3: Apoplastic pathway requires energy, while symplastic pathway does not, Option 4: Apoplastic pathway does not require energy, while symplastic pathway does, Correct Option: Option 1"
    },
    {
        "prompt": "Biology, Unit 8: Transport in plants, hard, What is guttation and how does it differ from transpiration?",
        "completion": "Option 1: Guttation is the exudation of drops of xylem sap on the tips or edges of leaves, typically occurring at night, while transpiration is the evaporation of water from plant surfaces, primarily from the stomata of leaves, Option 2: Guttation is the evaporation of water from plant surfaces, while transpiration is the exudation of drops of xylem sap, Option 3: Guttation occurs during the day, while transpiration occurs at night, Option 4: Guttation and transpiration are the same process, Correct Option: Option 1"
    }
]

file_name = "training_data.jsonl"

with open(file_name, "w") as output_file:
    for entry in training_data:
        json.dump(entry, output_file)
        output_file.write("\n")



