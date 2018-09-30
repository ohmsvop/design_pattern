import abc  # Python's built-in abstract class library

# FlyBehavior
class FlyBehavior(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def fly(self):
        """Required Method"""

class FlyWithWings(FlyBehavior):
    def fly(self):
        print "I'm flying!!"

class FlyNoWay(FlyBehavior):
    def fly(self):
        print "I can't fly"

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print "I'm flying with a rocket!"

fly_with_wings = FlyWithWings()
fly_no_way = FlyNoWay()
fly_rocket_powered = FlyRocketPowered()

# QuackBehavior
class QuackBehavior(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def quack(self):
        """Required Method"""

class Quack(QuackBehavior):
    def quack(self):
        print "QUACK"

class MuteQuack(QuackBehavior):
    def quack(self):
        print "<< Silence >>"

class Squeak(QuackBehavior):
    def quack(self):
        print "Squeak"

quack = Quack()
mute_quack = MuteQuack()
squeak = Squeak()

class Duck(object):
    def __init__(self, flyBehavior, quackBehavior):
        self._fly_behavior = flyBehavior
        self._quack_behavior = quackBehavior

    def performFly(self):
        self._fly_behavior.fly()

    def performQuack(self):
        self._quack_behavior.quack()

    def setFlyBehavior(self, flyBehavior): 
        self._fly_behavior = flyBehavior
        
    def setQuackBehavior(self, quackBehavior): 
        self._quack_behavior = quackBehavior

# Types of Ducks
class MallardDuck(Duck):
    def __init__(self):
        super(MallardDuck, self).__init__(fly_with_wings, quack)

    def display(self):
        print "I'm a real Mallard duck"

class ModelDuck(Duck):
    def __init__(self):
        super(ModelDuck, self).__init__(fly_no_way, quack)

    def display(self):
        print "I'm a model duck"


if __name__ == '__main__':
    mallard = MallardDuck()
    mallard.display()
    mallard.performQuack() # QUACK
    mallard.performFly() # I'm flying!!

    model = ModelDuck()
    model.display()
    model.performFly() # I can't fly
    model.setFlyBehavior(fly_rocket_powered)
    model.performFly() # I'm flying with a rocket!

