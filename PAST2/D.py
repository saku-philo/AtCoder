# https://atcoder.jp/contests/past202004-open/tasks/past202004_d


# 文字列Tが文字列Sにマッチするかを判定する関数
# マッチする時はTrueを、しない時はFalseを返す
def is_match(T, S):
    # 文字列Sのi文字目から始まる部分が文字列Tとマッチするかどうかを調べる
    for i in range(0, len(S) - len(T) + 1):
        # 文字列Sのi文字目か始まる部分が
        # Tとマッチしているかを保持する変数
        ok = True

        # 文字列Tのj文字目と、文字列Sのi+j文字目を見比べる
        for j in range(0, len(T)):
            # 文字列Tのj文字目が文字列Sのi+j文字目と異なっていた、
            # かつ、文字列TのJ文字目が"."でもない場合、
            # 文字列Sのi文字目から始まる部分は文字列Tとはマッチしない
            if S[i + j] != T[j] and T[j] != ".":
                ok = False

        # 文字列Sのi文字目から始まる部分が文字列Tとマッチしている場合
        # Trueを返す
        if ok:
            return True

    # 文字列Sの全ての部分について文字列Tとマッチしなかった場合、Falseを返す
    return False
