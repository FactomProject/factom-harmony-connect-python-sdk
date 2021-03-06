from unittest import TestCase
from factom_sdk.utils.key_common import KeyCommon


class TestKeyCommon(TestCase):
    def test_create_key_pair(self):
        """Check create key pair"""
        key_pair = KeyCommon.create_key_pair()
        self.assertTrue("private_key" in key_pair)
        self.assertTrue("public_key" in key_pair)
        key_pair_with_data = KeyCommon.create_key_pair("abcdefghijklmnopqrstuvwxyz123456")
        self.assertTrue("private_key" in key_pair_with_data)
        self.assertTrue("public_key" in key_pair_with_data)
        with self.assertRaises(Exception) as cm:
            KeyCommon.create_key_pair("abc")
            self.assertTrue("provided ed25519 private key is invalid." in str(cm.exception))

    def test_validate_checksum(self):
        """Check validate checksum"""
        key_passing = KeyCommon.validate_checksum("")
        self.assertFalse(key_passing)
        key_bytes_length_match = KeyCommon.validate_checksum("idpub2")
        self.assertFalse(key_bytes_length_match)
        key_valid = KeyCommon.validate_checksum("idpub2TWHFrWrJxVEmbeXnMRWeKBdFp7bEByosS1phV1bH7NS99zH12")
        self.assertFalse(key_valid)
        key_valid = KeyCommon.validate_checksum("idpub2TWHFrWrJxVEmbeXnMRWeKBdFp7bEByosS1phV1bH7NS99zHF9")
        self.assertTrue(key_valid)

    def test_get_invalid_keys(self):
        """Check get invalid keys"""
        missing_key = KeyCommon.get_invalid_keys([])
        self.assertEqual(missing_key, [])
        errors = [
            {
                "key": "123",
                "error": "key is invalid",
            },
            {
                "key": "123",
                "error": "key is invalid",
            },
        ]
        errors_key = KeyCommon.get_invalid_keys(["123", "123"])
        self.assertEqual(errors_key, errors)
        errors_key = KeyCommon.get_invalid_keys(["idpub2FEZg6PwVuDXfsxEMinnqVfgjuNS2GzMSQwJgTdmUFQaoYpTnv",
                                               "idpub1tkTRwxonwCfsvTkk5enWzbZgQSRpWDYtdzPUnq83AgQtecSgc"])
        self.assertEqual(errors_key, [])

    def test_get_duplicate_keys(self):
        """Check get duplicate keys"""
        missing_keys = KeyCommon.get_duplicate_keys([])
        self.assertEqual(missing_keys, [])
        errors = [
            {
                "key": "123",
                "error": "key is duplicated, keys must be unique.",
            },
        ]
        key_errors = KeyCommon.get_duplicate_keys(["123", "123"])
        self.assertEqual(errors, key_errors)

    def test_get_key_bytes_from_key(self):
        """Check get key bytes from key"""
        with self.assertRaises(Exception) as cm:
            KeyCommon.get_key_bytes_from_key("")
            self.assertTrue("key is invalid." in str(cm.exception))
        valid_key_bytes = KeyCommon.get_key_bytes_from_key("idpub2TWHFrWrJxVEmbeXnMRWeKBdFp7bEByosS1phV1bH7NS99zHF9")
        self.assertTrue(isinstance(valid_key_bytes, bytes))

    def test_get_public_key_from_private_key(self):
        """Check get public key from private key"""
        with self.assertRaises(Exception) as cm:
            KeyCommon.get_public_key_from_private_key("idsec2")
            self.assertTrue("signer_private_key is invalid." in str(cm.exception))
        public_key = KeyCommon.get_public_key_from_private_key("idsec1Xbja4exmHFNgVSsk7VipNi4mwt6BjQFEZFCohs4Y7TzfhHoy6")
        self.assertEqual(public_key, "idpub2TWHFrWrJxVEmbeXnMRWeKBdFp7bEByosS1phV1bH7NS99zHF9")

    def test_sign_content(self):
        """Check sign content"""
        with self.assertRaises(Exception) as cm:
            KeyCommon.sign_content("", "")
            self.assertTrue("signer_private_key is required." in str(cm.exception))
        with self.assertRaises(Exception) as cm:
            KeyCommon.sign_content("idsec1", "")
            self.assertTrue("signer_private_key is invalid." in str(cm.exception))
        with self.assertRaises(Exception) as cm:
            KeyCommon.sign_content("idsec1Xbja4exmHFNgVSsk7VipNi4mwt6BjQFEZFCohs4Y7TzfhHoy6", "")
            self.assertTrue("message is required." in str(cm.exception))
        signature = KeyCommon.sign_content("idsec1Xbja4exmHFNgVSsk7VipNi4mwt6BjQFEZFCohs4Y7TzfhHoy6", "Abc")
        self.assertEqual(signature,
                         "Z4qvla16B9+gW/IFyng+5Q0njgwT2aRr5kmYMARRbT8+nivUiQO74O/y3MOH42R9cqTdkXkETLDitUO48DviBw==")

    def test_validate_signature(self):
        """Check validate signature"""
        with self.assertRaises(Exception) as cm:
            KeyCommon.validate_signature("", "", "")
            self.assertTrue("signer_public_key is required." in str(cm.exception))
        with self.assertRaises(Exception) as cm:
            KeyCommon.validate_signature("idpub2", "", "")
            self.assertTrue("signer_public_key is invalid." in str(cm.exception))
        with self.assertRaises(Exception) as cm:
            KeyCommon.validate_signature("idpub2TWHFrWrJxVEmbeXnMRWeKBdFp7bEByosS1phV1bH7NS99zHF9", "", "")
            self.assertTrue("signature is required." in str(cm.exception))
        with self.assertRaises(Exception) as cm:
            KeyCommon.validate_signature("idpub2TWHFrWrJxVEmbeXnMRWeKBdFp7bEByosS1phV1bH7NS99zHF9",
                                       "D+lzNLb88IKXQk2BglvP7o6yK/DNAsO1B9qXdqArvrotTqSCI4Y4d8J8bwbfAyCvJT9tLYj9Ll7grCnyDWVtCg==",
                                       "")
            self.assertTrue("message is required." in str(cm.exception))
        valid_signature = KeyCommon.validate_signature("idpub2TWHFrWrJxVEmbeXnMRWeKBdFp7bEByosS1phV1bH7NS99zHF9",
                                                     "Z4qvla16B9+gW/IFyng+5Q0njgwT2aRr5kmYMARRbT8+nivUiQO74O/y3MOH42R9cqTdkXkETLDitUO48DviBw==",
                                                     "Abc")
        self.assertTrue(valid_signature)
        invalid_signature = KeyCommon.validate_signature("idpub2TWHFrWrJxVEmbeXnMRWeKBdFp7bEByosS1phV1bH7NS99zHF9",
                                                       "Z4qvla16B9+gW/IFyng+5Q0njgwT2aRr5kmYMARRbT8+nivUiQO74O/y3MOH42R9cqTdkXkETLDitUO48DviBw==",
                                                       "Abcd")
        self.assertFalse(invalid_signature)
