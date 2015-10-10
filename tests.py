import unittest
import pubsub


class TestPubSub(unittest.TestCase):
    def test_subscribe(self):
        sub = pubsub.subscribe('test')
        pubsub.publish('test', 'hello world')
        self.assertEqual(next(sub.listen())['data'], 'hello world')

    def test_unsubscribe(self):
        sub = pubsub.subscribe('test')
        pubsub.publish('test', 'hello world 1')
        sub.unsubscribe()
        pubsub.publish('test', 'hello world 2')
        msgs = list(sub.listen(block=False))
        self.assertEqual(len(msgs), 1)
        self.assertEqual(msgs[0]['data'], 'hello world 1')


if __name__ == '__main__':
    unittest.main()
