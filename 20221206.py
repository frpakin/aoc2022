
def unique(s):
    for i,c in enumerate(s):
        for j,d in enumerate(s):
            if i!=j and c==d:
                return False
    return True

def part1(s, limit=4):
    i = limit
    while i<len(s) and unique(s[i-limit:i])==False:
        i += 1
    return i

if __name__ == "__main__":
    input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    print(f'Test 1 (7): {part1(input)}')
    input = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    print(f'Test 1 (5): {part1(input)}')
    input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    print(f'Test 1 (11): {part1(input)}')

    puzzle = "dvgdvvbpbtbhbdhbhmmmcctmcmccggtrgghnhmnnqffpcprrqssnhsnhnshhsrsqqhchcdcfcqqcncrrzpppmzpzzhjzzzvrvnnpbpzzswzwswnngjgjgcjcfcllhffjbfjfhhppvnppfmfcmmcnnmnfnzfnzffphpnnnsvswvvnwnfntftjftfvvztzqzhzddttjpjbpphhlnnwgnwggdmmczclczzqddlcdldrlrccfflwwgqwwrjwrwzrrsdrrfssddcmmvrvlvhvfhfzhzbhbzzdmdvvsppwswmwdwjjzmzhhvghgthghvvtcthcttgsttpqpbbhthppzznntpnttshtshthhwrrgbbjzbjblblzbllcblcblbvvqfqqnjqqhfhftftwfftvvmddgzzmdzmdmtttttqmqmnqmqpmqpqqjlldpllfvlffjdfjjvlvjjjjbsjbjnnhmnhnrrwtrrfvvtppwmmpnnjbnjjcncjcttrcrjjlqjljccpzccvqvzzscctgccsmmnznhzhnnjggmjgmgjgtgtlgglhhrlhhrvhvrvtvvlvvwmmrjjzqqbzqqtgtzgttmgggwpgwgbwggwwprwwvswszznczncnccjnccjdjdjssqmmgcmcjmmhwhswhwdwrddtccmzmjmsmrmrddhrhhqbbspbsppqvqmvqmmclcddzjzvvslsffdhhqgqrqjrqjqjrrmpmrppcjpjffwhfwwppqvvzjzqqtftgfghgpglgnglldlvvwzwmmfzzhzmzhhswhhnvhvphpmphphrrwwfccmgmqgmmzgmgngznnzbzttjwttgngzzdndffwhfwhhlmllwqlwwgfgfpfnnldnldndbdcdddmbdmbbdpbpwbpptrrpggtrtrnttsmmcrmmlhltlgttblttbhttjzzvnnsbsqbqwbbtwtmtbbcjcljjslscswwglgqlgqgmmcpctcrttprpjjfvjfjqqljlvjljnnfhhfzhzmhmghhjnhjjbppmqqwlwswwgbbzszspzsppcscvvnhndhdwdmdrdssqrqdqsddnbnpplqppjbjdbdqdcccffsnntzntnmnlnbbrzzzvgvvqttbbzpbzpzdpdvppjmjpjbbdrbbgwgffzpzzjddmldlwwjdwwscwcfccnznmmfttvvmpmvpmvmcvmmjmwjwbbwqwjjzqjzjbbjqbjqqqthhsssmrsshvvprvvwccjlcctwwmgwgpwgpgcpptrppjppltlhthctttfptppwgpwprpbbqzbzznssfcsffbnnndffqmmqwmmpvvpvdppjqqttfpttjccbnbddvtdvddlsstjtccphchsswbbrqqgtqgqpqjqnjjvccwscwssjwjttqvtvmtmjjghghccpnpsplslmmfjfjtffgtgrtrftfhttpsttzzmhmllwqwhhnffdpffwbwnnbrrfbrrnjrjlljqqnjqnqqwlqqbbbtvvwgvgbgddpwdwvdwvdvvwzvwwtzwttppnttqccjtjrttqbbprpsrpssfjsffmdfmfbmbggjhggcjgcgvvjqqbhbllhrlhlclzzplpqqdtddrhhfssdvsvrrscsjjnwjjfpjfffcbfcfmmlpmphhhlpltptcpttppfssppgwppjgjnnblbhbtbrbgbpplnlvlsvlvwvwpptmtsswzswsnscsfcsfsfggzhghvvgbbfddgbbrmrtrqtthvhzhzthtbtjjcljjlcllzglzzdszdzjzjfzzzblbslbljjdnndvvnwnqnwqqscscmczcwwvrrlclttbtdtvddbrddvllnppvpmvmbbvfvttfcttggwgffrfwwwpwcpchppcrrgprgprgrjgjdgdgvddzndzdbzzswsvvtgtccrrnggbwggpjpnnsjjwfjjqfqvffrrhdrrsfrfjjfzfdzzqfqwbztszjqtttfdqvzmznzjlsjnwdthtwdtfslgdmgfpwsqcsqdhnsnsmghttfvlzqgspzdtlstdmthzftwmnqrznldpmwqbtthggjwcgjjmbpqgrnwspggjvrlcmtvpchmqhlwwtswqgpdjpbznqnssqhdjzgbjnfmgssrvnmmcvvhgmcvqbfdhgrhnqqzdmttmdzwgtprzqhplwnhhmlrvcbwpllqprtltdvqrwhvwzvlqsvfqsfjwmrnzlqpdgfpmtfdczqdnfjjbjmrdnffcmtwlzcmvnwmlpmqhvggdhptnzlvzwzwjbcszsnzgpwncfgvzfgbzwclvrbmllzpltzwjrftmppsfwhvvvhvqjtstnnczgtdbmpjjsscbdwplftgcgmtrnrnzplzhghrqgdtjwntwfstjwqjjrlhtwhnfqwfqgsjptjfpsrbnvvlgsltnvtfvscttwvrfzblzmfmnfrlrnzrrzhclggtntpjbbcphdvrfhnrtzvdmwbwgbftgzwlcqztghdhdmzwlmjbgptfnnzbmwsnzlzcpprqzmbbdsplmhpgmzthqcsfjcnfbfvsdsqzfvfcnpgqsvpgwsdbgjmsglrwmfjfpddczwvgdppfmrtszbtfdwbmlmzhqvvwmvlzvjfpffjnhwwhssfjnbzlqwqvjbjbhfntmhgswntdpbzlwwfbdbhrfhzfjsjbtlrqhlnrpfbwtpmrfvbhlmmsgtvcmrqmdpwvhqfqpgmfgnfrbvprhprtnpzjcnltndfsvjgndwblhwphtpsmnczgbtpwdvjsrctjbvbfslvslzlwbtstqvgcrqmfphwztpjqdmvcjpjqmjbdndfpzwsfwplchsmqwwbggptjdtztszmpfwgfwnqpdwfcpgrrhmfglsctjllflfltbcfvcpfcnqbwrvzmcmjpwptgsrlbrdchngwsdstfmcbrqvdsvvbnppdmnfwcgvpjjzqwcpvqfncvqlsfnjzprvhpgqscshqwsttdrsmqjfwlhcwlvnzvgvclqfjdgctvsrbwzflcldmrwlfhbgdtstqsqlblndnpgqlfbjzslcpcwvdwdffshhrzvhqwdsdmwtmtvcnrhmstvrnscppmbpmjbfjhljmsjnbjlhjhmnmcvvfgbdrblwbzrcctrjwjjwjtgnfjhhqbsmdjvdrdjtjbscfrsljnvqjlgjwqrvfmdttsvqjwdbswdtcfqsrpbvzrbsdqlqfjlrgcwzbqtqrpsrfcmbzcvjngcsmvqlbnghllcqcztbtvdrfcmpgfdprghsmbjvzbdnrdqnjdzslclgdsqglvpvcjpzqfwztlssljtmcdfcqdnqzwcttvpqfdpvzlhjfvvsgphgqrmzppvnjznqmdzfnfztjppstjfwddftcpcjnssznqbrvlvrzfhbvsjrwghttwlwfrptsvsrwfnvjtthwrppbngbgqvbsdgcrjcwjjljcwptrvgmbjpjtdbmhmzcfhzbsbrmzhdsrjbbmnwbsntpffdrrlgcrcgbcfwvlpmrzvsmvpjthtdjdvcspdsdvshlrwzcqnjmcnrgzbqzhfzbmtrvzzmjwbnjggtrtgcsnrmzbtjzgdmffdntspdhgnvgrmpbtnsspcqhsrvppjbrmdbggjbftnnbrgdsmdscqthdzflldfnplqccthpwccsfsnstttwztqnmnfshntqngmcndbsbftmgnhhwjvhchdfqzzgpdnfgvnjzjzfdzvsvtdqqcftrvmdcszcwpfrbcsmlqqfprrjgncwcvcngmrnwntcvzzlnwrhrznnldslhqdscbgsrqnvnmdtqvlttwqljmvbpbfldtbgzhvwzghnhwrwdqphhhgjpnmtlcmvfbdffnsvcswtmffzsrvczbntfpdsmwbqphvvcflpwgsrmjhrljlvzdgrcwpfphmvtwqwhjmrvmjzjlzlbflhzrdrzcdwhblpqwjljbvprddtvnccmchgctncwbpnmlqppfmhwchvjvpmblqhccfhlprdrczdfhmnsqhddbqlppgsnvhhfrwhqhfdpvsfcvzbqhgswtmnpmzrwsvnmztnqwdrhllssmgtzbztsprpsj"
    print(f'Part 1 (1965): {part1(puzzle)}')
    print(f'Part 2 (2773): {part1(puzzle, 14)}')