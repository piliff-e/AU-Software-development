print_string "Hello, world!";;

let a = 10;;
let foo a b = 
  match (a, b) with
  | (0, 1) -> "01"
  | _ -> "hehe";;

print_string (foo a 0);;
print_string (foo 0 1);;

let b = 5;;

if a <> b then print_int 0
else if a = b then print_string "1";;

(* let array = 1 :: 2 :: " hehe" :: true :: [];; *)

type 'a tree =
      | Leaf
      | Node of 'a * 'a tree * 'a tree;;

let cortej = (1, 2, "hehe", true);;
let list = 1 :: 2 :: 55 :: 8 :: [];;


let target = [];;
let rec imper f g list = 12 ;;

let rec fibonacci n =
  if n <= 1 then n
  else
    fibonacci (n - 1) + fibonacci (n - 2);;

let rec fibonacci2 n =
  match n with
  | 0 -> 0
  | 1 -> 1
  | _ -> fibonacci2 (n - 1) + fibonacci2 (n - 2);;

let rec fibonacci2 n = match n with 0 -> 0 | 1 -> 1 | _ -> fibonacci2 (n - 1) + fibonacci2 (n - 2);;

let list = 1;;
let n = 10;;  (* Задаем количество элементов *)
let lst = List.init n (fun i -> i);;  (* Создаем список от 0 до n-1 *)
let b  = List.map fibonacci lst;;

(*сумма списка*)
let rec list_summ l =
  match l with
    [] -> 0
  | h::t -> h + list_summ t;;

let spsk = 1::2::3::4::5::6::7::[];;

print_string "\n\n"; print_int (list_summ spsk); print_string "\n\n";;

let list1 = 1 :: 2 :: 55 :: 8 :: [];;
let list2 = [1;2;3;55;8];;

print_string "\n\n";;

(* Функция, которая применяет заданную функцию к каждому элементу списка *)
let apply_to_list f lst =
  List.map f lst;;

(* Примеры функций, которые мы хотим применить к списку *)
let double x = x * 2;;
let square x = x * x;;

(* Исходный список *)
let numbers = [1; 2; 3; 4; 5];;

(* Применение функции apply_to_list с функцией double *)
let doubled_numbers = apply_to_list double numbers;;

(* Применение функции apply_to_list с функцией square *)
let squared_numbers = apply_to_list square numbers;;

let rec print_list f l = match l with
    [] -> ()
  | h::[] -> f h
  | h::t -> f h; print_string ","; print_list f t;;

(* Вывод результатов *)
print_list print_int doubled_numbers;;
print_string "\n";;
print_list print_int squared_numbers;;

let rec fibonacci n =
  if n <= 1 then n
  else
    fibonacci (n - 1) + fibonacci (n - 2);;

let rec fibonacci2_1 n =
  match n with
  | 0 -> 0
  | 1 -> 1
  | _ -> fibonacci2 (n - 1) + fibonacci2 (n - 2);;

let rec fibonacci2_2 n = match n with 0 -> 0 | 1 -> 1 | _ -> fibonacci2 (n - 1) + fibonacci2 (n - 2);;
let rec list_summ lst =
  match lst with
    [] -> 0
  | h::t -> h + list_summ t;;

let rec gcd (a,b) =
  match (a,b) with
  | (0,b) -> b
  | (a,0) -> a
  | (a,b) -> if a < b then gcd ((b mod a),a)
                      else gcd ((a mod b),b);;

let rec fibonacci n =
  if n <= 1 then n
  else
    fibonacci (n - 1) + fibonacci (n - 2);;

let rec fibonacci2_1 n =
  match n with
  | 0 -> 0
  | 1 -> 1
  | _ -> fibonacci (n - 1) + fibonacci (n - 2);;

let rec fibonacci2_1 n = match n with 0 -> 0 | 1 -> 1 | _ -> fibonacci (n - 1) + fibonacci (n - 2);;


type color = Red | Blue | White | Black;;


type human =
  Name of string
| Age of int
| Height of float;;


type 'a tree =
  | Leaf
  | Node of 'a * 'a tree * 'a tree;;

  let add_one = fun x -> x + 1;;
    print_int (add_one 5);;  (* Вывод: 6 *)


(* Функция высшего порядка, которая применяет заданную функцию к каждому элементу списка *)
let apply_to_list f lst = List.map f lst;;

(* Функции первого класса, которые нужно применить к списку *)
let double x = x * 2;;
let square x = x * x;;

(* Исходный список *)
let numbers = [1; 2; 3; 4; 5];;

(* Применение функции apply_to_list с функцией double *)
let doubled_numbers = apply_to_list double numbers;;

(* Применение функции apply_to_list с функцией square *)
let squared_numbers = apply_to_list square numbers;;

(* Вывод результатов (print_list не встроена) *)
print_list print_int doubled_numbers;;
print_list print_int squared_numbers;;

let rec print_list f l = match l with
    [] -> ()
  | h::[] -> f h
  | h::t -> f h; print_string ","; print_list f t;;

  let a = 202;;  (* константа *)

  let foo x y = x + y;;
let foo_float x y = x +. y;;
(* Арифметика зависит от типа *)
let sum_int = foo 7 1;;
let sum_float = foo_float 2.4 0.03;;

print_string "Hello, world!";;
print_int 12;;
print_int (foo 2 5);;

(* if a <> b then print_int 0
else if a = b then print_string "1";; *)

let cortege = (1, 2, "hehe", true);;
let list1 = 1 :: 2 :: 55 :: 8 :: [];;
let list2 = [1;2;3;55;8];;
(*
def find_orfs(sequence):
    """
    Функция поиска всех ORF (открытых рамок считывания) в последовательности нуклеотидов
    :param sequence: последовательность нуклеотидов (тип string)
    :return: массив всех ORF
    """
    start_codon = ['ATG', 'AUG']
    stop_codons = ['TAA', 'TAG', 'TGA', 'UAA', 'UGA', 'UAG']
    orfs = []

    for i in range(len(sequence)):  # Проход по нуклеотидам в поиске старт-кодона
        if sequence[i:i+3] in start_codon:  # Найден старт-кодон
            for j in range(i+3, len(sequence), 3):  # Проход по нуклеотидам в поиске стоп-кодона
                if sequence[j:j+3] in stop_codons:  # Найден стоп-кодон
                    orfs.append(sequence[i:j+3])  # Добавление всего участка последовательности от старт- до стоп-кодона
                    break  # Переход к i+1-му нуклеотиду

    return orfs
*)
