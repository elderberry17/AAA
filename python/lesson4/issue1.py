from morse import encode, decode

if __name__ == '__main__':
    morse_msg = '-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.'
    # morse_msg = '123'
    decoded_msg = decode(morse_msg)
    assert morse_msg == encode(decoded_msg), "decoding function works incorrectly!"
