defmodule Day3 do
  @spec toInts(string()) :: list(integer())
  def toInts(str) do
    str
    |> String.graphemes()
    |> Enum.map(&String.to_integer/1)
  end

  @spec bitwiseSum(list(integer()), list(integer())) :: list(integer())
  def bitwiseSum(acc, next) do
    Stream.zip(acc, next)
    |> Enum.map(fn {a, b} -> a + b end)
  end

  @spec bnot(integer()) :: integer()
  def bnot(1), do: 0
  def bnot(0), do: 1

  def bnot(_other) do
    throw("Bad input!")
  end

  def exec(input) do
    mid = Enum.count(input) / 2

    gamma =
      input
      |> Stream.map(&Day3.toInts/1)
      |> Enum.reduce(&Day3.bitwiseSum/2)
      |> Enum.map(fn
        x when x > mid -> 1
        _ -> 0
      end)

    epsilon =
      gamma
      |> Enum.map(&Day3.bnot/1)

    IO.puts(
      Integer.undigits(gamma, 2) *
        Integer.undigits(epsilon, 2)
    )
  end
end

File.stream!("~/workspace/adventofcode-2021/Day3/input_day3.txt")
|> Stream.map(&String.trim/1)
|> Day3.exec()
